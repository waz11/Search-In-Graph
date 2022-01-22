from abc import ABC, abstractmethod
from Result.result import Result

class ISearcher(ABC):
    @abstractmethod
    def search(self) -> Result:
        pass

