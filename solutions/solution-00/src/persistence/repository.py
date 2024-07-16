""" Repository pattern for data access layer """

from abc import ABC, abstractmethod
from src import app
from src.persistence.db import DBRepository
from src.persistence.file import FileRepository


class Repository(ABC):
    """Abstract class for repository pattern"""

    @abstractmethod
    def reload(self) -> None:
        """Reload data to the repository"""

    @abstractmethod
    def get_all(self, model_name: str) -> list:
        """Get all objects of a model"""

    @abstractmethod
    def get(self, model_name: str, id: str) -> None:
        """Get an object by id"""

    @abstractmethod
    def save(self, obj) -> None:
        """Save an object"""

    @abstractmethod
    def update(self, obj) -> None:
        """Update an object"""

    @abstractmethod
    def delete(self, obj) -> bool:
        """Delete an object"""
