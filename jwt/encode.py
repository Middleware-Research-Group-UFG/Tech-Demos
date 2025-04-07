import jwt
from os import getenv
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta


key = getenv("SECRET_KEY")

payload = {
	"user": "bob",
	"role": "student",
	"iat": datetime.now(ZoneInfo("UTC")),
	"nbf": datetime.now(ZoneInfo("UTC")) + timedelta(minutes=2),
	"exp": datetime.now(ZoneInfo("UTC")) + timedelta(hours=3, minutes=2)
}

algorithm = "HS256"


token = jwt.encode(payload, key, algorithm)
print(token)
