from fastapi import FastAPI
from .domains.books.presentation.book_controller import router as book_router
from .domains.auth.presentation.auth_controller import router as auth_router
from .domains.users.presentation.user_controller import router as user_router

app = FastAPI()

app.include_router(book_router)
app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}