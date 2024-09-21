from abc import ABC, abstractmethod

class BaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_data(self):
        pass
