import jwt

payload = {"user": "admin"}
secret = "test"  # You can change this to any key you want
token = jwt.encode(payload, secret, algorithm="HS256")

print("JWT token:")
print(token)