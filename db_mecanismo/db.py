from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL ='mysql+pymysql://appuser:SenhaForteAqui@127.0.0.1:3306/appdb?charset=utf8mb4'
engine = create_engine(
    url= DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(bind=engine , expire_on_commit= False)