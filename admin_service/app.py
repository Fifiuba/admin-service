from fastapi import FastAPI
import uvicorn
from admin_service.controllers import admin_controller


app = FastAPI()
app.include_router(admin_controller.admin_route)


@app.get("/")
async def root():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
