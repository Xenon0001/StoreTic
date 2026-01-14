# Desktop application main entry point
import customtkinter as ctk
from api_client import get_products, create_product, create_sale, get_sales_summary
from login_window import LoginWindow
from tkinter import messagebox

# Configuración inicial
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("StoreTic Admin")
app.geometry("480x420")

# --- 1. DEFINIR VARIABLES GLOBALES Y ESTADO ---
_products_cache = []

# --- 2. DEFINIR FUNCIONES DE LA LÓGICA ---
def refresh():
    """Actualizar lista de productos y opciones"""
    global _products_cache
    
    # Intentar obtener datos (Protegido)
    try:
        _products_cache = get_products()
    except Exception as e:
        # Si falla la conexión, cache vacío y aviso silencioso en consola o popup
        print(f"Error conexión: {e}")
        _products_cache = []

    # Limpiar UI
    products_box.delete("1.0", "end")
    names = []

    # Procesar datos (Protegido contra datos corruptos)
    try:
        if not _products_cache:
            products_box.insert("end", "No se pudieron cargar productos o no hay inventario.\n")
        
        for p in _products_cache:
            # Usar .get para evitar errores si faltan claves
            p_id = p.get('id', '?')
            p_name = p.get('name', 'Sin nombre')
            p_stock = p.get('stock', 0)
            p_price = p.get('price', 0)
            
            info = f"{p_id}: {p_name} — Stock: {p_stock} — Precio: {p_price}\n"
            products_box.insert("end", info)
            names.append(f"{p_id} - {p_name}")
            
    except Exception as e:
        products_box.insert("end", f"Error visualizando datos: {e}\n")

    # Actualizar selector
    if names:
        product_option.configure(values=names)
        product_option.set(names[0])
    else:
        product_option.configure(values=["(sin productos)"])
        product_option.set("(sin productos)")

def add_product():
    try:
        data = {
            "name": name_entry.get().strip(),
            "price": float(price_entry.get()),
            "stock": int(stock_entry.get())
        }
    except ValueError:
        messagebox.showerror("Error", "Precio y Stock deben ser números")
        return

    try:
        create_product(data)
        # Limpiar campos
        name_entry.delete(0, "end")
        price_entry.delete(0, "end")
        stock_entry.delete(0, "end")
        refresh()
        messagebox.showinfo("Listo", "Producto creado")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear: {e}")

def sell_selected():
    sel = product_option.get()
    if not sel or sel.startswith("(sin"):
        return

    try:
        p_id = int(sel.split(" - ")[0])
        qty = int(quantity_entry.get())
        if qty <= 0: raise ValueError("Cantidad debe ser positiva")
        
        create_sale([{"product_id": p_id, "quantity": qty}])
        
        quantity_entry.delete(0, "end")
        refresh()
        messagebox.showinfo("Venta", "Venta exitosa")
    except ValueError:
        messagebox.showerror("Error", "Revisa la cantidad")
    except Exception as e:
        messagebox.showerror("Error API", str(e))

def show_sales_report():
    try:
        summary = get_sales_summary()
        
        # Ventana popup
        rw = ctk.CTkToplevel(app)
        rw.title("Reporte")
        rw.geometry("300x200")
        # Fix para que la ventana reporte quede encima
        rw.attributes('-topmost', True) 
        
        ctk.CTkLabel(rw, text="Resumen de Ventas", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkLabel(rw, text=f"Ventas Totales: {summary.get('total_sales_count', 0)}").pack()
        ctk.CTkLabel(rw, text=f"Ingresos: ${summary.get('total_amount', 0):.2f}").pack()
        
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener reporte: {e}")

# --- 3. CONSTRUIR INTERFAZ (UI) ---

# Sección Agregar
ctk.CTkLabel(app, text="Agregar producto").pack(pady=(5, 0))
name_entry = ctk.CTkEntry(app, placeholder_text="Nombre")
name_entry.pack(pady=2)
price_entry = ctk.CTkEntry(app, placeholder_text="Precio")
price_entry.pack(pady=2)
stock_entry = ctk.CTkEntry(app, placeholder_text="Stock")
stock_entry.pack(pady=2)
ctk.CTkButton(app, text="Guardar Nuevo", command=add_product).pack(pady=5)

# Sección Venta
ctk.CTkLabel(app, text="Ventas").pack(pady=(10, 0))
product_option = ctk.CTkOptionMenu(app, values=["Cargando..."])
product_option.pack(pady=2)
quantity_entry = ctk.CTkEntry(app, placeholder_text="Cantidad")
quantity_entry.pack(pady=2)
ctk.CTkButton(app, text="Registrar Venta", fg_color="green", command=sell_selected).pack(pady=5)
ctk.CTkButton(app, text="Ver Informe", fg_color="gray", command=show_sales_report).pack(pady=2)

# Lista Productos
products_box = ctk.CTkTextbox(app, height=100)
products_box.pack(pady=10, padx=10, fill="both", expand=True)

# --- 4. GESTIÓN DE ARRANQUE Y LOGIN ---

app.withdraw()
login_window = LoginWindow(app)
app.wait_window(login_window.window)

if login_window.is_authenticated():
    # 1. Primero mostramos la ventana
    app.deiconify()
    
    # 2. Forzamos a que se dibuje la interfaz (evita la ventana en blanco)
    app.update_idletasks()
    app.update()
    
    # 3. Ahora que la ventana existe y es visible, cargamos datos
    try:
        refresh()
    except Exception as e:
        print(f"Error inicializando datos: {e}")
        
    # 4. Iniciamos el bucle principal
    app.mainloop()
else:
    app.quit() # Usa quit() en lugar de destroy() para cerrar el hilo
    exit()