from fastapi import FastAPI, Depends
from src.auth import get_current_user

app = FastAPI()


@app.get("/protected_route")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}!"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")