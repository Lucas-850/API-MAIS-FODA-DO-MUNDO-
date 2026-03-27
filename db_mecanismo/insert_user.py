from db import SessionLocal
from models import User

with SessionLocal.begin() as session:
    user = User(name= 'Lucas', email ='lucasrodrigues@gmail.com')
    session.add(user)


print('Usuário adicionado')