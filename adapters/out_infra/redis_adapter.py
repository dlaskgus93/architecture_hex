# adapters/out_infra/redis_adapter.py
from core.ports import CachePort

class RedisAdapter(CachePort): # 계약서 상속
    def save(self, key: str, value: str):
        print(f"[Redis 어댑터] {key}에 {value}를 임시 저장했습니다!")