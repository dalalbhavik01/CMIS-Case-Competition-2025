import sys
import os

# Setup environment
sys.path.append(os.path.join(os.getcwd(), "backend"))
os.environ["DATABASE_URL"] = "sqlite:///cmis.db"

from database import SessionLocal
from models import User

def approve_user(email):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            print(f"Approving user: {user.email}")
            user.is_active = True
            db.commit()
            print("User approved!")
        else:
            print(f"User {email} NOT FOUND.")
    finally:
        db.close()

if __name__ == "__main__":
    approve_user("dalalbhavik012@gmail.com")
