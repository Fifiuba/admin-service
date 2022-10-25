import uvicorn
from admin_service.app import app
from admin_service.security import firebase
from admin_service.database import database,config



database.init_database()
database.insert_super_admin(config.db_admin)
firebase.init_firebase()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
