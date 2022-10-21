import uvicorn
import app
from admin_service.security import firebase


firebase.init_firebase()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
