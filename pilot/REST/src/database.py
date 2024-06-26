from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class InventoryDB(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True, index=True)
    time = Column(BigInteger, nullable=False)
    flight = Column(String(256), nullable=False)
    departure = Column(BigInteger, nullable=False)
    flight_booking_class = Column(Text, nullable=False)
    idle_seats_count = Column(Integer, nullable=False)

class Database:
    def __init__(self):
        self.db_username = os.environ.get('POSTGRES_USER')
        self.db_password = os.environ.get('POSTGRES_PASSWORD')
        self.db_name = os.environ.get('POSTGRES_DB')
        self.db_host = os.environ.get('POSTGRESS_HOST')

        if not all([self.db_username, self.db_password, self.db_name, self.db_host]):
            raise ValueError("Missing one or more environment variables: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRESS_HOST")

        self.SQLALCHEMY_DATABASE_URL = f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}/{self.db_name}"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
