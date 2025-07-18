from fastapi import FastAPI
from .routes import router as main_router
from .metrics import setup_metrics

def create_app():
    app = FastAPI(
        title="Store API",
        description="API para gestionar clientes, productos y ventas",
        version="1.0.0"
    )

    app.include_router(main_router)
    setup_metrics(app)

    return app
