from db import Base, engine
from apps.models import Item

Base.metadata.create_all(engine)
