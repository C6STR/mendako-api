import json
import UserLogin

ul = UserLogin.UserLogin()

data = {
    "mail_address" : "test@test.com",
    "password" : "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
}

json = json.dumps(data)

res = ul.user_login(json)
print(res)