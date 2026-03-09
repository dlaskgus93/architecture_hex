# core/ports.py (계약서)
from abc import ABC, abstractmethod

# 💡 외부 장비들이 지켜야 할 계약서
class StoragePort(ABC):
    @abstractmethod
    def upload(self, file_name: str) -> str: pass

class CachePort(ABC):
    @abstractmethod
    def save(self, key: str, value: str): pass

# 💡 데이터를 주고받을 때 쓸 우리 회사만의 '표준 규격'
class StandardModelData:
    def __init__(self, name: str):
        self.name = name