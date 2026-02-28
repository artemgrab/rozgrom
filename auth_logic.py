import bcrypt
from sqlalchemy.orm import Session
import models

# Hashes the password
def hash_password(password: str):

    #! Upper bound for password length (71), should be added to /signup
    pwd_bytes = password.encode("utf-8")[:71]
    hashed = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())

    return hashed.decode("utf-8")

# Verifies whether the password is correct
def verify_password(plain_password: str, hashed_password: str):

    password_bytes = plain_password.encode("utf-8")[:71]
    hash_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hash_bytes)


# Addes user to database
def add_user(db: Session, user_data: dict):

    # Hashes password 
    hashed_pwd = hash_password(user_data["password"])

    # Creates new user instance
    new_user = models.User(
        full_name=user_data["full_name"],
        username=user_data["username"],
        email=user_data["email"],
        hashed_password=hashed_pwd
    )
    
    # Addes new_user instance to database
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Automatically generates ID and join_time 
        
        print("New user adde successfully")
        return new_user
        
    except Exception as e:
        db.rollback()
        return {"error": f"Could not create user: {str(e)}"}
    
    
    