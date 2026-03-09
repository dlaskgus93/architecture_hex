# main.py
from fastapi import FastAPI
from adapters.out_infra.s3_adapter import S3Adapter
from adapters.out_infra.redis_adapter import RedisAdapter
from core.model_service import ModelService
from adapters.in_fastapi.api_v1 import get_v1_router
from adapters.in_fastapi.api_v2 import get_v2_router

app = FastAPI()

# 🛠️ 1. 부품(어댑터)들을 만듭니다.
s3_worker = S3Adapter()
redis_worker = RedisAdapter()

# 🛠️ 2. 핵심 로직에 부품을 끼워 넣습니다. (의존성 주입)
my_service = ModelService(storage=s3_worker, cache=redis_worker)

# 🛠️ 3. 라우터(문)를 열어줍니다.
app.include_router(get_v1_router(my_service))
app.include_router(get_v2_router(my_service))