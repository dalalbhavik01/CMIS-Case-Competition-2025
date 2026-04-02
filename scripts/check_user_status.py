import sys
import os

# Setup environment
sys.path.append(os.path.join(os.getcwd(), "backend"))
os.environ["DATABASE_URL"] = "sqlite:///cmis.db"

from database import SessionLocal
from models import User

def check_user(email):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            print(f"User Found: {user.email}")
            print(f"  Active: {user.is_active}")
            print(f"  Verified: {user.verification_token is None}")
            print(f"  Token: {user.verification_token}")
        else:
            print(f"User {email} NOT FOUND.")
    finally:
        db.close()

if __name__ == "__main__":
    check_user("dalalbhavik012@gmail.com")
