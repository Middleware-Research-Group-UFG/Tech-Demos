import db


user = {
    "tag": "cyber_bob",
    "name": "Bob",
    "email": "rbcmlproject@gmail.com",
    "password": "hello_world"
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

model = {
    "name": "School news",
    "description": "This model can be used by schools to announce news",
    "roles": [role1, role2, role3]
}

print(db.create_user(user))
print(db.create_model(model))

