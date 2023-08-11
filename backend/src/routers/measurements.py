

from fastapi import APIRouter

from managers.measurement import MeasurementManager

import db
from schemas.request.measurement import MeasurementModel

router = APIRouter(tags=['Measurements'])


@router.get('/')
async def ping():
    return {'ping': 'success'}


@router.get('/measurements/')
async def measurement(body: MeasurementModel):
    return await MeasurementManager.get_measurements(body)


@router.post('/measurements/')
async def measurement(body: MeasurementModel):
    return await MeasurementManager.add_measurements(body)
