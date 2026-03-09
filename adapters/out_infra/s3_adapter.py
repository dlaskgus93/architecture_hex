# adapters/out_infra/s3_adapter.py
from core.ports import StoragePort

class S3Adapter(StoragePort): # 계약서 상속
    def upload(self, file_name: str) -> str:
        print(f"[S3 어댑터] {file_name} 파일을 S3 창고에 저장했습니다!")
        return f"s3://bucket/{file_name}"