from fastapi import APIRouter

from models.suma import Suma

router = APIRouter()


@router.post("/suma")  # entrada como JSON
async def suma(suma: Suma):
    return {"resultado": suma.a + suma.b}


@router.get("/suma")  # entrada como query params
async def suma(a: int, b: int):
    return {"resultado": a + b}
