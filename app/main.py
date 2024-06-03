from fastapi import FastAPI
from .domains.books.presentation.book_controller import router as book_router

app = FastAPI()

app.include_router(book_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}