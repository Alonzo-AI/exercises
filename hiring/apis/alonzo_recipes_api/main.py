from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import recipes

app = FastAPI(title="Alonzo Recipes API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Alonzo Recipes API"}