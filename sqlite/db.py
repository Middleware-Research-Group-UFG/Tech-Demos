import sqlite3


db = "rbcml.db"

def create_user(user):
    with sqlite3.connect(db) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        try:
            query = f"""INSERT INTO User 
                           VALUES {tuple(user.values())}"""
            cursor.execute(query)
            return f"User {user['tag']} created successfully!"

        except Exception as e:
            return f"Error: {e}"

def create_model(model):
    with sqlite3.connect(db) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()

        try:
            query = f"""INSERT INTO MODEL (Name, Description) 
                            VALUES ("{model['name']}", "{model['description']}")"""
            cursor.execute(query)
            model_id = cursor.lastrowid

            for role in model['roles']:
                query = f"""INSERT OR IGNORE INTO Capability (SVideo, Rvideo, SAudio, RAudio, SString, RString) 
                                VALUES {role['capabilities']}"""
                cursor.execute(query)
                if cursor.rowcount == 0:
                               capabilities = role['capabilities']
                               query = f"""SELECT Id FROM Capability WHERE SVideo = {capabilities[0]} AND 
                                                                         RVideo = {capabilities[1]} AND 
                                                                         SAudio = {capabilities[2]} AND 
                                                                         RAudio = {capabilities[3]} AND 
                                                                         SString = {capabilities[4]} AND 
                                                                         RString = {capabilities[5]}"""
                               cursor.execute(query)
                               capability_id = cursor.fetchone()[0]
                               query = f"""INSERT INTO Role (Name, ModelId, CapabilityId) 
                                                VALUES ("{role['name']}", {model_id}, {capability_id})"""
                               cursor.execute(query)
                else:
                    capability_id = cursor.lastrowid
                    query = f"""INSERT INTO Role (Name, ModelId, CapabilityId)
                                    VALUES ("{role['name']}", {model_id}, {capability_id})"""
                    cursor.execute(query)

            return "Model created successfully!"
                  
        except Exception as e:
            return f"Error: {e}"

def create_session(session):
    with sqlite3.connect(db) as connection:
        connection.execute("PRAGMA foreign_key = ON")
        cursor = connection.cursor() 
        try:
            participants = session['participants']
            del session['participants']
            query = f"""INSERT INTO Session {tuple(session.keys())}
                            VALUES {tuple(session.values())}"""
            cursor.execute(query)
            session_id = cursor.lastrowid
            for participant in participants:
                query = f"""INSERT INTO Participant
                                VALUES {tuple(participant.values()) + (session_id,)}"""
                cursor.execute(query)
            return "Session created successfully!"
        
        except Exception as e:
            return f"Error: {e}"
