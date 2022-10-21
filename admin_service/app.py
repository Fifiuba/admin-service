from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from admin_service.controllers import admin_controller


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_controller.admin_route, prefix="/admins", tags=["Admins"])


@app.get("/")
async def read_items():
    return {"token": "Hola"}
