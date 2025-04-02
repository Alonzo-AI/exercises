from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products, categories

app = FastAPI(title="Alonzo Store Admin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Alonzo Store Admin API"}