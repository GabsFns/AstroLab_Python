from fastapi import FastAPI
from app.routes import routes

app = FastAPI(
    title="AstroLab - Astro Data Processo",
)

app.include_router(routes)