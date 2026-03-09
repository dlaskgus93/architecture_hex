# adapters/in_fastapi/api_v2.py
from fastapi import APIRouter
from core.model_service import ModelService
from core.ports import StandardModelData

def get_v2_router(service: ModelService):
    router = APIRouter()

    @router.post("/v2/model")
    def save_v2(payload: dict):
        # 🌟 통역사의 역할: v2의 복잡한 데이터를 '표준 데이터'로 번역해서 넘김!
        standard_data = StandardModelData(name=payload["metadata"]["name"])
        return service.save_model_logic(standard_data)

    return router