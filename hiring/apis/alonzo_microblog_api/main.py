from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import posts

app = FastAPI(title="Alonzo Microblog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Alonzo Microblog API"}