from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('SQLITE_URL')

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

with engine.connect() as cuonn :
    print(cuonn.execute(text("SELECT 1")).scalar_one())
    print(cuonn.execute(text("SELECT DATABASE()")).scalar_one())