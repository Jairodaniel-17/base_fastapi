from fastapi import APIRouter

from models.suma import Suma

router = APIRouter()


@router.post("/suma")
async def suma(suma: Suma):
    return {"resultado": suma.a + suma.b}
