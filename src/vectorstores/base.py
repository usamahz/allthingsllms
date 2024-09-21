from abc import ABC, abstractmethod

class BaseVectorStore(ABC):
    @abstractmethod
    def index(self, data):
        pass

    @abstractmethod
    def search(self, query, k=1):
        pass
