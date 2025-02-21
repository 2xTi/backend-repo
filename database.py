from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = "postgres"
password = "tiagoreis123"
database = "database_tigas"
host = "localhost"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


try:
    with engine.connect() as conn:
        print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")

