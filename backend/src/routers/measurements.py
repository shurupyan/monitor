from fastapi import APIRouter

from managers.measurement import MeasurementManager

import db
from schemas.request.measurement import MeasurementModel

router = APIRouter(tags=["Measurements"])


@router.get("/")
async def ping():
    return {"ping": "success"}


# @router.get("/measurements/")
# async def get_measurement():
#     return await MeasurementManager.get_measurements()


@router.post("/measurements/")
async def post_measurement(body: MeasurementModel):
    return await MeasurementManager.add_measurements(body)
