from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./historico.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SimulacaoDB(Base):
    __tablename__ = "simulacoes"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, index=True)
    resultado = Column(String)
    limite_liberado = Column(Float)

Base.metadata.create_all(bind=engine)