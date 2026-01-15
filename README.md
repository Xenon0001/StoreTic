# StoreTic
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![CustomTkinter](https://img.shields.io/badge/Desktop-CustomTkinter-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)


Sistema de **gestión de ventas e inventario** diseñado para pequeños comercios.

StoreTic permite administrar productos, registrar ventas y generar reportes desde una aplicación de escritorio,
con un backend centralizado y una arquitectura escalable que puede crecer para integrar interfaces web
y otros clientes.

---

## 🚀 Tabla de Contenidos

- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estado del Proyecto](#estado-del-proyecto)
- [Mejoras Futuras](#mejoras-futuras)
- [Autor](#autor)

---

## 🧾 Descripción

StoreTic es una solución desarrollada para comercios locales que necesitan digitalizar sus operaciones básicas sin depender de herramientas complejas o internet estable.

La aplicación de escritorio (administrador) se comunica con un backend API que procesa y almacena la información en una base de datos PostgreSQL. Esta arquitectura permite integrar otras interfaces (como web o móvil) en el futuro sin cambiar la lógica de negocio.

---

<!-- ## 🖼️ Capturas de Pantalla

### Pantalla de Login
![Login](screenshots/login.png)

### Panel Principal
![Dashboard](screenshots/dashboard.png)

### Reporte de Ventas
![Sales Report](screenshots/sales_report.png)


--- -->

## 🏗️ Arquitectura

```
┌───────────────────────────┐
|        Desktop App        |
|  (CustomTkinter / Python) |
└─────────────┬─────────────┘
              |
              | HTTP (API REST)
              ↓
┌───────────────────────────┐
|         Backend API       |
|          (FastAPI)        |
└─────────────┬─────────────┘
              |
              | SQLAlchemy ORM
              ↓
┌───────────────────────────┐
| PostgreSQL Database       |
└───────────────────────────┘
```

---

## ✔️ Características

- ✅ Autenticación de administrador
- ✅ Gestión de productos (Crear, Leer, Actualizar, Eliminar)
- ✅ Registro de ventas con control automático de inventario
- ✅ Reportes básicos de ventas
  - Total de ventas
  - Total monetario
  - Promedio por venta
- 🔄 Arquitectura desacoplada para escalabilidad

---

## 🛠️ Instalación

### Requisitos

Asegúrate de tener instalados:

- Python 3.10+
- PostgreSQL
- Git

---

### Paso a paso (local)

1. **Clonar el repositorio**
  ```bash
    git clone https://github.com/Xenon0001/StoreTic.git
    cd StoreTic
  ````

2. **Configurar entorno backend**
> En Windows
  ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
  ```

3. **Configurar PostgreSQL**
- Crear base de datos: storetic
- Crear usuario con permisos
- Ajustar DATABASE_URL en el backend

4. **Inicializar tablas**
  ```bash
    python -c "from db import Base, engine; Base.metadata.create_all(bind=engine)"
  ```

5. **Iniciar servidor**
  ```bash
    cd backend
    uvicorn main:app --reload
  ```

6. **Inicializar tablas**
  ```bash
    cd desktop
    python main.py
  ```

---

## 🔐 Configuración de Entorno

El backend utiliza variables de entorno para la conexión a la base de datos.

Ejemplo de `DATABASE_URL`: postgresql://usuario:password@localhost:5432/storetic

---

## 👨‍💻 Uso
### Pantalla de Login
- Ingresa con tus credenciales de administrador.

### Gestión de Productos
- Crear, editar o eliminar productos.
- Control de stock.

### Registro de Ventas
- Seleccionar producto(s)
- Ingresar cantidad
- Registrar venta con descuento automático de inventario.

### Reportes
- Ver métricas de ventas desde la opción “Informe de Ventas”.

---

## 🗂️ Estructura del Proyecto
```
  StoreTic/
  │
  ├── .ai/
  │   ├──status_reports/        # Reportes de estado
  │   └── ...                   # Ingeniería de contexto
  │
  ├── backend/                  # API REST (FastAPI)
  │   ├── routers/
  │   ├── models.py
  │   ├── schemas.py
  │   ├── db.py
  │   └── main.py
  ├── desktop/                  # Aplicación de escritorio
  │   ├── main.py
  │   └── api_client.py
  ├── .gitignore
  └── README.md
```

---

## 📌 Estado del Proyecto

### 📍 MVP funcional.
Actualmente el proyecto soporta:

- CRUD de productos
- Registro de ventas
- Reportes básicos
- Autenticación de administrador
- Integración backend–desktop

---

## 📈 Mejoras Futuras

- UI web para clientes o vendedores
- Reportes con gráficas
- Exportar reportes a PDF/Excel
- Autenticación consolidada (roles)
- Implementar API pública para clientes web

---

## 👤 Autor
Luis Rafael Eyoma
