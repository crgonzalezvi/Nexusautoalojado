from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

class Venta(BaseModel):
    id: int
    cliente_id: int
    producto_id: int
    cantidad: int

clientes: List[Cliente] = []
productos: List[Producto] = []
ventas: List[Venta] = []

@app.get("/")
def home():
    return {"mensaje": "API de Gestión de Clientes, Productos y Ventas"}

@app.get("/clientes")
def listar_clientes():
    return clientes

@app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente

@app.get("/productos")
def listar_productos():
    return productos

@app.post("/productos")
def crear_producto(producto: Producto):
    productos.append(producto)
    return producto

@app.get("/ventas")
def listar_ventas():
    return ventas

@app.post("/ventas")
def crear_venta(venta: Venta):
    ventas.append(venta)
    return venta
