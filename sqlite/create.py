import db
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

user_alice = {
    "Tag": "cyber_alice",
    "Name": "Alice",
    "Email": "rbcmlproject@gmail.com",
    "Password": "HeLl0_w0rLd!"
}

user_bob = {
    "Tag": "cyber_bob",
    "Name": "Bob",
    "Email": "rbcmlproject@gmail.com",
    "Password": "hello_world"
}

model1 = {
    "Name": "School news",
    "Description": "This model can be used by schools to announce news",
    "Definition": """{
                        "roles": ["Student", "Professor", "Principal"],
                        "connections":[
                            {
                                "Principal-Professor-Student": [
                                    [true, true, true, true, true, true, true, false],
                                    [false, true, true, true, true, true, true, false],
                                    [false, true, false, true, true, true, false, true]
                                ]
                            },
                            {   
                                "Principal-Professor": [
                                    [true, true, true, true, true, true, true, false],
                                    [true, true, true, true, true, true, false, true]
                                ]
                            },
                            {
                                "Professor-Student": [
                                    [true, true, true, true, true, true, true, false],
                                    [false, true, true, true, true, true, false, true]
                                ]
                            }
                        ]
                    }"""
}

session1 = {
    "Creator": "cyber_alice",
    "ModelId": 1,
    "ExpirationDate": str(datetime.now(ZoneInfo("UTC")) + timedelta(days=3))[0:19],
    "Participants": """{ 
                          "cyber_alice": ["Principal"],  
                          "cyber_bob": ["Professor", "Student"]
                        }"""
}

print(db.create_user(user_alice))
print(db.create_user(user_bob))
print(db.create_model(model1))
print(db.create_session(session1))

