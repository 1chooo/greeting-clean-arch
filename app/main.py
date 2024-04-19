from fastapi import FastAPI, status

from app.infra.web.router import setup_routers

app = FastAPI()
setup_routers(app)

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}
