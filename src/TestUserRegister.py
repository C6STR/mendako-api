import json
import UserRegister

ur = UserRegister.UserRegister()

data = {
    "mail_address" : "test@test.com",
    "user_name" : "テストマン",
    "password" : "password"
}

json = json.dumps(data)

ur.user_register(json)