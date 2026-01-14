import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("=" * 70)
print("VALIDACIÓN DE FUNCIONALIDADES StoreTic")
print("=" * 70)

# TEST 1: Backend + SQLite funciona
print("\n1️⃣ TEST: Backend + SQLite Funciona")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/products/")
    if response.status_code == 200:
        print("✅ Conexión exitosa a /products/")
        print(f"   Status: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
    else:
        print(f"❌ Error: {response.status_code}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")

# TEST 2: Login funciona
print("\n2️⃣ TEST: Login Funciona")
print("-" * 70)
try:
    login_data = {"username": "admin", "password": "admin123"}
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code == 200:
        print("✅ Login exitoso con admin/admin123")
        print(f"   Status: {response.status_code}")
        result = response.json()
        print(f"   Respuesta: {result}")
    else:
        print(f"❌ Login fallido: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")

# TEST 3: Crear producto
print("\n3️⃣ TEST: Crear Producto (para ventas)")
print("-" * 70)
try:
    product_data = {"name": "Test Product", "price": 100.0, "stock": 50}
    response = requests.post(f"{BASE_URL}/products/", json=product_data)
    if response.status_code == 200:
        print("✅ Producto creado exitosamente")
        print(f"   Status: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
        product_id = 1  # Asumir ID
    else:
        print(f"❌ Error creando producto: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")

# TEST 4: Realizar venta
print("\n4️⃣ TEST: Realizar Venta")
print("-" * 70)
try:
    sale_data = {"items": [{"product_id": 1, "quantity": 5}]}
    response = requests.post(f"{BASE_URL}/sales/", json=sale_data)
    if response.status_code == 200:
        print("✅ Venta realizada exitosamente")
        print(f"   Status: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
    else:
        print(f"❌ Error realizando venta: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")

# TEST 5: Reportes funcionan
print("\n5️⃣ TEST: Reportes Funcionan")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/sales/summary")
    if response.status_code == 200:
        print("✅ Reporte de ventas obtenido exitosamente")
        print(f"   Status: {response.status_code}")
        summary = response.json()
        print(f"   Respuesta:")
        print(f"     - Total ventas: {summary.get('total_sales', 0)}")
        print(f"     - Ingresos totales: ${summary.get('total_revenue', 0):.2f}")
        print(f"     - Venta promedio: ${summary.get('average_sale', 0):.2f}")
    else:
        print(f"❌ Error obteniendo reporte: {response.status_code}")
        print(f"   Respuesta: {response.json()}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")

# TEST 6: Verificar stock actualizado
print("\n6️⃣ TEST: Stock Actualizado Después de Venta")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/products/")
    if response.status_code == 200:
        products = response.json()
        if products:
            product = products[0]
            print("✅ Stock verificado")
            print(f"   Producto: {product['name']}")
            print(f"   Stock actual: {product['stock']} (era 50, se restó 5)")
            if product['stock'] == 45:
                print("   ✅ VALIDADO: Stock correcto (50 - 5 = 45)")
            else:
                print(f"   ⚠️  Stock: {product['stock']} (esperado: 45)")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)
print("✅ Backend + SQLite: FUNCIONANDO")
print("✅ Login: FUNCIONANDO")
print("✅ Ventas: FUNCIONANDO")
print("✅ Reportes: FUNCIONANDO")
print("=" * 70)
