from fastapi import APIRouter

from src.healthcheck.schemes import HealthCheck

router = APIRouter()


@router.get('/healthcheck')
def healthcheck() -> HealthCheck:
    return HealthCheck()
