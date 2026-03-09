# adapters/in_fastapi/api_v1.py
from fastapi import APIRouter
from core.model_service import ModelService
from core.ports import StandardModelData

def get_v1_router(service: ModelService):
    router = APIRouter()

    @router.post("/v1/model")
    def save_v1(payload: dict):
        # 🌟 통역사의 역할: v1 허접한 데이터를 '표준 데이터'로 번역해서 넘김!
        standard_data = StandardModelData(name=payload["model_name"])
        return service.save_model_logic(standard_data)

    # 새로운 API 라우터 추가
    @router.get("/v1/model/{model_name}")
    def get_model(model_name: str):
        return service.get_model_status(model_name)

    return router