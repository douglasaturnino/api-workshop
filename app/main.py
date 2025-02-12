from fastapi import FastAPI

from app.config import engine
from app.model import Base
from app.routers import router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)
