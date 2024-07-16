"""
User related functionality
"""

from src.models.base import Base
from src import db, bcrypt


class User(Base):
    """User representation"""
    
    __table__ = "users"

    email = db.Column(db.String(128), nullable=False, unique=True)
    hash_password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email: str, password: str, first_name: str, last_name: str, is_admin: bool = False, **kw):
        """Dummy init"""
        super().__init__(**kw)
        self.email = email
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        
   

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
    def set_password(self, password):
        self.hash_password = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.hash_password, password)
        
    @staticmethod
    def create(user: dict) -> "User":
        """Create a new user"""
        from src.persistence import repo

        users: list["User"] = User.get_all()

        for u in users:
            if u.email == user["email"]:
                raise ValueError("User already exists")

        new_user = User(**user)

        repo.save(new_user)

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> "User | None":
        """Update an existing user"""
        from src.persistence import repo

        user: User | None = User.get(user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "password" in data:
            user.set_password = data["password"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "is_admin" in data:
            user.is_admin = data["is_admin"]

        repo.update(user)

        return user
