"""Ventana de login para StoreTic Desktop"""
import customtkinter as ctk
from tkinter import messagebox
from api_client import login, APIError

class LoginWindow:
    """Ventana modal de login"""
    
    def __init__(self, parent_app):
        self.parent_app = parent_app
        self.authenticated = False
        
        # Crear ventana
        self.window = ctk.CTkToplevel(parent_app)
        self.window.title("StoreTic - Login")
        self.window.geometry("300x200")
        self.window.resizable(False, False)
        
        # Hacerla modal
        self.window.transient(parent_app)
        self.window.grab_set()
        
        # Centrar ventana
        self.window.attributes('-topmost', True)
        
        # Crear UI
        self._create_ui()
        
    def _create_ui(self):
        """Crear elementos de la interfaz"""
        # Título
        title_label = ctk.CTkLabel(
            self.window,
            text="Iniciar Sesión",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)
        
        # Usuario
        ctk.CTkLabel(self.window, text="Usuario:").pack(pady=(10, 0))
        self.username_entry = ctk.CTkEntry(
            self.window,
            placeholder_text="admin"
        )
        self.username_entry.pack(pady=5, padx=20, fill="x")
        self.username_entry.focus()
        
        # Contraseña
        ctk.CTkLabel(self.window, text="Contraseña:").pack(pady=(10, 0))
        self.password_entry = ctk.CTkEntry(
            self.window,
            placeholder_text="Contraseña",
            show="●"
        )
        self.password_entry.pack(pady=5, padx=20, fill="x")
        
        # Botón Login
        login_button = ctk.CTkButton(
            self.window,
            text="Iniciar Sesión",
            command=self._handle_login,
            fg_color="#1f6aa5"
        )
        login_button.pack(pady=20)
        
        # Permitir login con Enter
        self.password_entry.bind("<Return>", lambda e: self._handle_login())
        
    def _handle_login(self):
        """Procesar intento de login"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Error", "Completa usuario y contraseña")
            return
        
        try:
            if login(username, password):
                self.authenticated = True
                self.window.destroy()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrecto")
                self.password_entry.delete(0, "end")
        except APIError as e:
            messagebox.showerror("Error de conexión", str(e))
    
    def is_authenticated(self) -> bool:
        """Retorna True si el login fue exitoso"""
        return self.authenticated
