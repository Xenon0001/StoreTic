# Desktop application main entry point
import customtkinter as ctk
from api_client import get_products, create_product, create_sale, get_sales_summary
from login_window import LoginWindow
from tkinter import messagebox

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("StoreTic Admin")
app.geometry("480x420")
app.withdraw()  # Ocultar hasta que se autentique

# Mostrar login
login_window = LoginWindow(app)
app.wait_window(login_window.window)

# Si no se autenticó, cerrar app
if not login_window.is_authenticated():
    app.destroy()
    exit()

# Mostrar app después de autenticar
app.deiconify()

# Formulario para crear productos
name_entry = ctk.CTkEntry(app, placeholder_text="Nombre")
price_entry = ctk.CTkEntry(app, placeholder_text="Precio")
stock_entry = ctk.CTkEntry(app, placeholder_text="Stock")

# Selección y venta
product_option = ctk.CTkOptionMenu(app, values=["(cargando...)"])
quantity_entry = ctk.CTkEntry(app, placeholder_text="Cantidad")

products_box = ctk.CTkTextbox(app, height=140)

# Estado local
_products_cache = []

def refresh():
    """Actualizar lista de productos y opciones"""
    global _products_cache
    try:
        _products_cache = get_products()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener productos:\n{e}")
        _products_cache = []

    products_box.delete("1.0", "end")
    names = []
    for p in _products_cache:
        products_box.insert("end", f"{p['id']}: {p['name']} — Stock: {p['stock']} — Precio: {p['price']}\n")
        names.append(f"{p['id']} - {p['name']}")

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
    except Exception:
        messagebox.showerror("Error", "Datos de producto inválidos")
        return

    try:
        resp = create_product(data)
        if resp is not None and getattr(resp, 'status_code', 200) >= 400:
            messagebox.showerror("Error", f"Error creando producto: {resp.text}")
            return
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear producto:\n{e}")
        return

    name_entry.delete(0, "end")
    price_entry.delete(0, "end")
    stock_entry.delete(0, "end")
    refresh()
    messagebox.showinfo("Listo", "Producto creado")

def sell_selected():
    sel = product_option.get()
    if not sel or sel.startswith("(sin"):
        messagebox.showwarning("Seleccionar", "Selecciona un producto")
        return

    try:
        product_id = int(sel.split(" - ")[0])
    except Exception:
        messagebox.showerror("Error", "Producto seleccionado inválido")
        return

    try:
        qty = int(quantity_entry.get())
    except Exception:
        messagebox.showerror("Error", "Cantidad inválida")
        return

    if qty <= 0:
        messagebox.showerror("Error", "La cantidad debe ser mayor que 0")
        return

    sale_items = [{"product_id": product_id, "quantity": qty}]
    try:
        resp = create_sale(sale_items)
        if resp is not None and getattr(resp, 'status_code', 200) >= 400:
            messagebox.showerror("Error", f"Error en la venta: {resp.text}")
            return
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo completar la venta:\n{e}")
        return

    quantity_entry.delete(0, "end")
    refresh()
    messagebox.showinfo("Venta", "Venta registrada correctamente")

def show_sales_report():
    """Abrir ventana de informe de ventas"""
    try:
        summary = get_sales_summary()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener el informe:\n{e}")
        return
    
    # Crear ventana de informe
    report_window = ctk.CTkToplevel(app)
    report_window.title("Informe de ventas")
    report_window.geometry("400x200")
    
    # Labels con datos
    ctk.CTkLabel(report_window, text="Informe de Ventas", font=("Arial", 16, "bold")).pack(pady=20)
    
    total_count = summary.get("total_sales_count", 0)
    total_amount = summary.get("total_amount", 0.0)
    average_sale = summary.get("average_sale", 0.0)
    
    ctk.CTkLabel(report_window, text=f"Total de ventas: {total_count}", font=("Arial", 12)).pack(pady=5)
    ctk.CTkLabel(report_window, text=f"Total dinero: ${total_amount:.2f}", font=("Arial", 12)).pack(pady=5)
    ctk.CTkLabel(report_window, text=f"Promedio por venta: ${average_sale:.2f}", font=("Arial", 12)).pack(pady=5)
    
    ctk.CTkButton(report_window, text="Cerrar", command=report_window.destroy).pack(pady=15)

# Layout
ctk.CTkLabel(app, text="Agregar producto").pack(pady=(8, 0))
name_entry.pack(pady=4)
price_entry.pack(pady=4)
stock_entry.pack(pady=4)
ctk.CTkButton(app, text="Agregar", command=add_product).pack(pady=6)

ctk.CTkLabel(app, text="\nVender producto").pack(pady=(8, 0))
product_option.pack(pady=4)
quantity_entry.pack(pady=4)
ctk.CTkButton(app, text="Vender", fg_color="#1f6aa5", command=sell_selected).pack(pady=6)

ctk.CTkButton(app, text="Informe de Ventas", fg_color="#2d6a4f", command=show_sales_report).pack(pady=6)

ctk.CTkLabel(app, text="\nProductos").pack(pady=(8, 0))
products_box.pack(pady=6, padx=8, fill="both")


refresh()
app.mainloop()
