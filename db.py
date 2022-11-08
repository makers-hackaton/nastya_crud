from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://nastya:1@127.0.0.1/fast_api_test")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
