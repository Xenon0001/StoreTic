# StoreTic

StoreTic es un sistema de gestión de ventas e inventario diseñado para pequeños comercios.
Permite administrar productos y registrar ventas desde una aplicación de escritorio,
con un backend centralizado que almacena y procesa los datos.

El proyecto está pensado para entornos locales, con arquitectura clara, desacoplada
y preparada para crecer hacia una interfaz web.

---

## 🧠 Descripción General

StoreTic utiliza una arquitectura cliente-servidor:

- El **administrador** trabaja desde una aplicación de escritorio.
- Todas las operaciones se envían a un **backend REST**.
- Los datos se almacenan en una **base de datos PostgreSQL**.
- La información puede ser consumida por otros clientes (web, reportes, etc.).

Este enfoque permite centralizar los datos y mantener consistencia entre plataformas.

---

## 🏗️ Arquitectura del Sistema

Desktop App (CustomTkinter)
|
| HTTP (API REST)
v
Backend (FastAPI)
|
| ORM (SQLAlchemy)
v
Database (PostgreSQL)


---

## ⚙️ Stack Tecnológico

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- CustomTkinter
- Uvicorn

---

## 🚀 Funcionalidades Principales

- Autenticación de administrador
- Gestión de productos (CRUD)
- Registro de ventas
- Reporte de ventas:
  - Total de ventas
  - Total de ingresos
  - Promedio por venta
- Arquitectura desacoplada (backend independiente del cliente)

---

## 🖥️ Componentes del Proyecto

- `backend/`  
  API REST desarrollada con FastAPI.

- `desktop/`  
  Aplicación de escritorio desarrollada con CustomTkinter.

---

## 🛠️ Instalación (Resumen)

1. Crear y activar entorno virtual
2. Instalar dependencias
3. Configurar PostgreSQL
4. Ejecutar el backend
5. Ejecutar la aplicación de escritorio

> La guía detallada se documentará en futuras versiones.

---

## 📌 Estado del Proyecto

- MVP funcional
- Backend y Desktop integrados
- Base de datos PostgreSQL operativa
- Proyecto estable y extensible

---

## 👤 Autor

Luis Rafael Eyoma  
Proyecto desarrollado como parte de la iniciativa **Xenon.py**.
