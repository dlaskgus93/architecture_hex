# core/model_service.py (핵심 로직)
from core.ports import StoragePort, CachePort, StandardModelData

class ModelService:
    # 생성할 때 일꾼(어댑터)들을 전달받음 (의존성 주입)
    def __init__(self, storage: StoragePort, cache: CachePort):
        self.storage = storage
        self.cache = cache

    # 🌟 핵심: v1인지 v2인지 모름! 오직 '표준 규격(StandardModelData)'만 받음!
    def save_model_logic(self, data: StandardModelData):
        print(f"\n--- [헥사고날] 표준 데이터({data.name}) 저장 로직 시작 ---")
        
        # S3인지 구글인지 모르고 그냥 upload 시킴
        s3_url = self.storage.upload(data.name)
        self.cache.save(f"model:{data.name}", "STATUS_OK")
        
        return {"status": "success", "url": s3_url}

    # 👉 3. 새로운 API 추가 시 기능만 순수하게 만듦
    def get_model_status(self, model_name: str):
        print(f"\n--- [헥사고날] {model_name} 조회 로직 시작 ---")
        return {"model": model_name, "status": "STATUS_OK"}