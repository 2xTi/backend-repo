import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Ler variáveis de ambiente com fallback
user = os.getenv("DB_USER", "default_user")
password = os.getenv("DB_PASSWORD", "default_password")
database = os.getenv("DB_NAME", "default_db")
host = os.getenv("DB_HOST", "postgres")  # ✅ Fallback para o nome do serviço

# Debug: Verificar variáveis carregadas
print(f"DB_USER={user}")
print(f"DB_PASSWORD={'*' * len(password) if password else None}")
print(f"DB_NAME={database}")
print(f"DB_HOST={host}")

# Construir a URL de conexão
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

# Criar engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Testar conexão
try:
    with engine.connect() as conn:
        print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
