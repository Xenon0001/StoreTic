# API client for desktop application
import requests
from typing import List, Dict, Any

API_URL = "http://127.0.0.1:8000"

class APIError(Exception):
    """Error de conexión con la API"""
    pass

def _make_request(method: str, endpoint: str, **kwargs):
    """Helper para hacer requests con manejo de errores"""
    try:
        url = f"{API_URL}{endpoint}"
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        raise APIError("No se pudo conectar al servidor. ¿Está corriendo FastAPI?")
    except requests.exceptions.Timeout:
        raise APIError("Timeout de conexión. El servidor tardó demasiado en responder.")
    except requests.exceptions.HTTPError as e:
        raise APIError(f"Error del servidor: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.RequestException as e:
        raise APIError(f"Error en la solicitud: {str(e)}")

# PRODUCTOS
def get_products() -> List[Dict[str, Any]]:
    """Obtener lista de productos"""
    return _make_request("GET", "/products")

def create_product(data: Dict[str, Any]) -> Dict[str, Any]:
    """Crear un nuevo producto"""
    return _make_request("POST", "/products", json=data)

# VENTAS
def create_sale(items: List[Dict[str, int]]) -> Dict[str, Any]:
    """Crear una venta. items: [{"product_id": 1, "quantity": 2}, ...]"""
    payload = {"items": items}
    return _make_request("POST", "/sales", json=payload)

def get_sale(sale_id: int) -> Dict[str, Any]:
    """Obtener detalles de una venta específica"""
    return _make_request("GET", f"/sales/{sale_id}")

def list_sales() -> List[Dict[str, Any]]:
    """Obtener lista de todas las ventas"""
    return _make_request("GET", "/sales")
def get_sales_summary() -> Dict[str, Any]:
    """Obtener resumen de ventas"""
    return _make_request("GET", "/sales/summary")

# AUTENTICACIÓN
def login(username: str, password: str) -> bool:
    """Autenticar usuario. Retorna True si es válido, False si no"""
    try:
        result = _make_request("POST", "/auth/login", json={"username": username, "password": password})
        return result.get("success", False)
    except APIError:
        return False

def get_pending_orders():
    response = requests.get(f"{API_URL}/orders/pending")
    response.raise_for_status()
    return response.json()


def confirm_order(order_id: int):
    response = requests.post(f"{API_URL}/orders/{order_id}/confirm")
    response.raise_for_status()
    return response.json()


def cancel_order(order_id: int):
    response = requests.post(f"{API_URL}/orders/{order_id}/cancel")
    response.raise_for_status()
    return response.json()

