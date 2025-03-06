from abc import ABC, abstractmethod


class BaseClassMe(ABC):
    @abstractmethod
    def __str__(self):
        pass
