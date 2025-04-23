import db
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

user1 = {
    "tag": "cyber_bob2",
    "name": "Bob",
    "email": "rbcmlproject@gmail.com",
    "password": "hello_world"
}

user2 = {
    "tag": "cyber_alice2",
    "name": "Alice",
    "email": "rbcmlproject@gmail.com",
    "password": "HeLl0_w0rLd!"
}

role1 = {
    "name": "Principal",
    "capabilities": (True, True, True, True, True, True)
}

role2 = {
    "name": "Professor",
    "capabilities": (True, True, True, True, True, True)
}

role3 = {
    "name": "Student",
    "capabilities": (False, True, False, True, True, True)
}

model1 = {
    "name": "School news",
    "description": "This model can be used by schools to announce news",
    "roles": [role1, role2, role3]
}

participant1 = {
    "role": 1,
    "userTag": "cyber_alice" 
}

participant2 = {
    "role": 3,
    "userTag": "cyber_bob"
}

session1 = {
    "creator": "cyber_alice",
    "modelId": 1,
    "expirationDate": str(datetime.now(ZoneInfo("UTC")) + timedelta(days=3))[0:19],
    "participants": [participant1, participant2]
}

print(db.create_user(user1))
print(db.create_user(user2))
print(db.create_model(model1))
print(db.create_session(session1))

