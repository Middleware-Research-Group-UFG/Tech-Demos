import jwt
from os import getenv


key = getenv("SECRET_KEY")

options = {
    "require": ["user", "role", "nbf", "exp"],
    "verify_signature": True,
    "verify_exp": "verify_signature",
    "verify_nbf": "verify_signature"
}

algorithm = "HS256"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYm9iIiwicm9sZSI6InN0dWRlbnQiLCJpYXQiOjE3NDQwNTI4NDcsIm5iZiI6MTc0NDA1Mjk2NywiZXhwIjoyNjA4MDYzNzY3fQ.bNhs_Ou18aA-6m50x91-dA7HdVcar-2P0byDMbDXLjY"


try:
	payload = jwt.decode(token, key, algorithm, options)
	print(payload)

except jwt.exceptions.ImmatureSignatureError:
	print("Token not valid yet.")

except jwt.exceptions.ExpiredSignatureError:
    print("Token not valid anymore.")

except jwt.exceptions.MissingRequiredClaimError:
    print("Missing required claim.")

except jwt.exceptions.InvalidSignatureError:
    print("Signature doesn't match.")

except Exception as e:
    print(e)
