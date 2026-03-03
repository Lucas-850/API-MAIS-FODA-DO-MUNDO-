from sqlalchemy import create_engine, text

DATABASE_URL = 'mysql+pymysql://appuser:SenhaForteAqui@127.0.0.1:3306/appdb?charset=utf8mb4'

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

with engine.connect() as cuonn :
    print(cuonn.execute(text("SELECT 1")).scalar_one())
    print(cuonn.execute(text("SELECT DATABASE()")).scalar_one())