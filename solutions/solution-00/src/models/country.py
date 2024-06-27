"""
Country related functionality
"""
from src import db
from src.models.base import Base
from src.models.city import City
from src.models.user import User

class Country:
    """
    Country representation

    This class does NOT inherit from Base, you can't delete or update a country

    This class is used to get and list countries
    """

    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(3), nullable=False, primary_key=True)
    cities = db.Column(db.List(db.String(128)))
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)

    def __init__(self, name: str, code: str, user_id: str, cities: list, **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)
        self.name = name
        self.code = code
        self.user_id = user_id
        self.cities = cities

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
            "cities": self.cities,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get_all() -> list["Country"]:
        """Get all countries"""
        from src.persistence import repo

        countries: list["Country"] = repo.get_all("country")

        return countries

    @staticmethod
    def get(code: str) -> "Country | None":
        """Get a country by its code"""
        for country in Country.get_all():
            if country.code == code:
                return country
        return None

    @staticmethod
    def create(name: str, code: str) -> "Country":
        """Create a new country"""
        from src.persistence import repo

        country = Country(name, code)

        repo.save(country)

        return country
