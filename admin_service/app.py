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


@app.get("/")
def welcome():
    data = {'service': 'Administrator service!',
    'created_on':'9-9-2022',
    'description':'Admin service is the responsable of manage admins'}
    return data

app.include_router(admin_controller.admin_route, prefix="/admins", tags=["Admins"])
