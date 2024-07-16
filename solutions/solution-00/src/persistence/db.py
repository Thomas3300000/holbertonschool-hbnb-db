"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from src import db


class DBRepository(Repository):
    """Database implementation"""
   
    def __init__(self) -> None:
        db.create_all()
        
    def get_all(self, model_name: str) -> list:
        """Get all objects of a given model"""
        if model_name in db.session:
            return db.session.query(model_name).all()
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Get an object by its ID"""
        if model_name in db.session:
            return db.session.query(model_name).get(obj_id)
        return None

    def reload(self) -> None:
        pass

    def save(self, obj: Base) -> None:
        """Save a new object in a database"""
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Base) -> Base | None:
        """Update an object in a databese"""
        db.session.commit()

    def delete(self, obj: Base) -> bool:
        """Delete an object in a database"""
        if obj in db.session:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False
