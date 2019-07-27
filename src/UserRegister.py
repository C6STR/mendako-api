import Db
import json
import hashlib
import uuid

class UserRegister():
    def __init__(self):
        self.db = Db.connect()

    def user_register(self , json_data):
        cur = self.db.cursor()
        data = json.loads(json_data)

        # uuid
        user_uuid = str(uuid.uuid4())

        # passwordハッシュ化
        # SHA256
        password_hash = hashlib.sha256(data["password"].encode()).hexdigest()

        sql = """
                insert into `user`(
                    user_id ,
                    mail_address ,
                    user_name ,
                    password
                )values(
                    '%s',
                    '%s',
                    '%s',
                    '%s'
                )
            """
        cur.execute(sql %(
            user_uuid ,
            data["mail_address"],
            data["user_name"],
            password_hash
        ))

        self.db.commit()