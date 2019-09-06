import UserAuthToken
import json

uat = UserAuthToken.UserAuthToken()

data = {
  "user_id" : "80d4a28f-e928-4b3a-b250-0c4665cc1bb6",
  "access_token" : "abcb03ea-861c-4a47-b900-6e380971fc10"
}

json = json.dumps(data)

res = uat.user_auth_token(json)

print(res)