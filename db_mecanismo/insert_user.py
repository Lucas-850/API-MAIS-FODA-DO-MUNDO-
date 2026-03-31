from db import SessionLocal
from models import User, Task

with SessionLocal.begin() as session:
    u = User(name="Lucas", email="lucas+tasks@exemplo.com")
    session.add(u)
    session.flush()  # garante u.id gerado

    session.add_all([
        Task(title="Task 1", user_id=u.id),
        Task(title="Task 2", user_id=u.id),
    ])

print("Inseriu user e tasks.")