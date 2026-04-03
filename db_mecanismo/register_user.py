from sqlalchemy.exc import IntegrityError
from db import SessionLocal
from models import User
from security import hash_password

def to_public_user(u: User) -> dict:
    return {"id":u.id, "name":u.name, "email":u.email}

def register_user(name:str, email: str, password:str) -> dict:
    with SessionLocal.begin() as session:
        u = User(
            name= name,
            email = email,
            password_hash = hash_password(password)
        )
        session.add(u)
        try:
            session.flush()
        except IntegrityError:
            raise ValueError("Email já cadastrado.")
        return to_public_user(u)
    
if __name__ == "__main__":
    created = register_user("Lucas", "lucas.reg@exemplo.com", "SenhaForte123!")
    print(created)