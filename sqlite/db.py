import sqlite3


db = "rbcml.db"

def create_user(user):
    with sqlite3.connect(db) as connection:
        cursor = connection.cursor()
        try:
            query = f"""INSERT INTO User 
                           VALUES {tuple(user.values())}"""
            cursor.execute(query)
            return f"User {user['Tag']} created successfully!"

        except Exception as e:
            return f"Error: {e}"

def create_model(model):
    with sqlite3.connect(db) as connection:
        cursor = connection.cursor()

        try:
            query = f"""INSERT INTO Model {tuple(model.keys())}  
                            VALUES {tuple(model.values())}"""
            cursor.execute(query)
            return "Model-{cursor.lastrowid} created successfully!"
                  
        except Exception as e:
            return f"Error: {e}"

def create_session(session):
    with sqlite3.connect(db) as connection:
        connection.execute("PRAGMA foreign_key = ON")
        cursor = connection.cursor() 
        try:
            query = f"""INSERT INTO Session {tuple(session.keys())}
                            VALUES {tuple(session.values())}"""
            cursor.execute(query)
            return "Session-{cursor.lastrowid} created successfully!"
        
        except Exception as e:
            return f"Error: {e}"

