from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('SQLITE_URL')
engine = create_engine(                         
    url= DATABASE_URL,
    echo=True,
    hide_parameters=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(bind=engine , expire_on_commit= False)