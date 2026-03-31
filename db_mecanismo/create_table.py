from db import engine
from models import Base, User, Task  # IMPORTANTE: garantir que User e Task foram carregados

Base.metadata.create_all(bind=engine)

print("Tabelas no metadata:", list(Base.metadata.tables.keys()))
print("Tabelas criadas/garantidas no banco.")