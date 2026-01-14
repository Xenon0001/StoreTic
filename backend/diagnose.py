# Script de diagnóstico para PostgreSQL
import os
import sys

print("=" * 60)
print("DIAGNÓSTICO - StoreTic PostgreSQL")
print("=" * 60)

# Verificar credenciales en db.py
print("\n1. Verificando credenciales en db.py...")
with open("db.py", "r") as f:
    db_content = f.read()
    print(f"   Contenido actual de DATABASE_URL:")
    for line in db_content.split("\n"):
        if "DATABASE_URL" in line:
            print(f"   {line}")

print("\n2. ¿Cómo configuraste PostgreSQL?")
print("   Opciones:")
print("   A) usuario/password por defecto (postgres/postgres)")
print("   B) usuario/password personalizado")
print("   C) Conexión sin contraseña (trust authentication)")

print("\n3. Para proceder, necesito que:")
print("   - Verifiques el usuario y contraseña de PostgreSQL")
print("   - Verifiques que existe la base de datos 'storetic'")
print("   - Actualices db.py con las credenciales correctas")
print("\n   Formato: postgresql://USUARIO:PASSWORD@localhost/storetic")
print("\n   Ejemplos:")
print("   - postgresql://postgres:postgres@localhost/storetic")
print("   - postgresql://postgres:@localhost/storetic (sin password)")

print("\n" + "=" * 60)
print("Presiona Enter cuando hayas actualizado db.py")
input()
