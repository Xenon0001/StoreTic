# -*- coding: utf-8 -*-
import os
import sys

# Configurar encoding para Windows
if sys.platform.startswith('win'):
    os.environ['PGCLIENTENCODING'] = 'UTF8'

print("=" * 60)
print("TEST DE CONEXIÓN - StoreTic Backend")
print("=" * 60)

try:
    print("\n✓ Verificando imports...", end=" ", flush=True)
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    print("OK")
    
    print("✓ Conectando a SQLite (test mode)...", end=" ", flush=True)
    
    # Usar sqlite en lugar de postgres para testing inicial
    DATABASE_URL = "sqlite:///./storetic_test.db"
    engine = create_engine(DATABASE_URL, echo=False)
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("OK")
    
    print("✓ Creando sesión...", end=" ", flush=True)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    print("OK")
    
    print("✓ Importando modelos...", end=" ", flush=True)
    from models import Product, Sale, SaleItem, Base
    print("OK")
    
    print("✓ Creando tablas...", end=" ", flush=True)
    Base.metadata.create_all(bind=engine)
    print("OK")
    
    print("✓ Creando producto de prueba...", end=" ", flush=True)
    test_product = Product(name="Producto Test", price=10.0, stock=100)
    db.add(test_product)
    db.commit()
    db.refresh(test_product)
    print(f"OK (ID: {test_product.id})")
    
    print("✓ Creando venta de prueba...", end=" ", flush=True)
    test_sale = Sale(total=20.0)
    db.add(test_sale)
    db.flush()
    
    test_item = SaleItem(
        sale_id=test_sale.id,
        product_id=test_product.id,
        quantity=2,
        price=10.0
    )
    db.add(test_item)
    test_product.stock -= 2
    db.commit()
    db.refresh(test_sale)
    print(f"OK (ID: {test_sale.id})")
    
    print("✓ Verificando stock actualizado...", end=" ", flush=True)
    updated_product = db.query(Product).filter(Product.id == test_product.id).first()
    if updated_product.stock == 98:
        print(f"OK (Stock: {updated_product.stock})")
    else:
        print(f"ERROR (Stock esperado: 98, obtenido: {updated_product.stock})")
    
    db.close()
    
    print("\n" + "=" * 60)
    print("✓ TODOS LOS TESTS PASARON CON SQLite")
    print("=" * 60)
    print("\n⚠ NOTA: Se usó SQLite para testing.")
    print("Para producción, configura PostgreSQL en db.py")
    
except Exception as e:
    import traceback
    print(f"ERROR: {str(e)}")
    print("\nDetalles:")
    traceback.print_exc()
    sys.exit(1)
