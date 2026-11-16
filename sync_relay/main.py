"""Juntitos Sync Relay API.

Servicio liviano de retransmisión de eventos HLC entre los dispositivos de la pareja.
Opera de forma local ($0 costo) y ciega (E2EE payload agnostic).
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Juntitos Sync Relay",
    version="0.1.0",
    description="Local-First Sync Relay para el hogar de Sebi y Alepz",
)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Healthcheck endpoint para validar que el relay está activo en la red."""
    return HealthResponse(
        status="ok",
        service="juntitos-sync-relay",
        version="0.1.0",
    )


@app.get("/")
def root():
    return {
        "message": "Juntitos Sync Relay activo 💑",
        "docs": "/docs",
    }
