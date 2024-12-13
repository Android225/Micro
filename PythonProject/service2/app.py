from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

DATABASE_URL = "postgresql://postgres:password@db:5432/mydb"

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Создаем таблицы в БД
Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

@app.get("/data")
def read_data():
    db = SessionLocal()
    items = db.query(Item).all()
    return {"items": [item.name for item in items]}

@app.post("/add_item")
def add_item(name: str):
    db = SessionLocal()
    new_item = Item(name=name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": f"Item {new_item.name} added"}
