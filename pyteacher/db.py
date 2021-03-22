import os

from pymongo import MongoClient


class PyTeacherDB:
    def __init__(self, db="db"):
        self._mongo = None
        self._db = db

    def __enter__(self):
        self._mongo = MongoClient(
            "mongodb://{user}:{pwd}@pyteacher_mongo:27017/".format(
                user=os.getenv("MONGO_USER"),
                pwd=os.getenv("MONGO_PASS"),
            )
        )
        self._db = self._mongo[self._db]
        return self

    def __exit__(self, _, __, ___):
        self._mongo.close()

    def get_user(self, telegram_user_id):
        return self._db["users"].find_one({"telegram_user_id": telegram_user_id})

    def exists_user(self, telegram_user_id):
        return self.get_user(telegram_user_id) is not None

    def add_user(self, user):
        if self.exists_user(user.telegram_user_id):
            return False
        try:
            self._db["users"].insert_one(user.dict())
            return True
        except Exception:
            return False

    def remove_user(self, telegram_user_id):
        try:
            self._db["users"].find_one_and_delete(
                {"telegram_user_id": telegram_user_id}
            )
            return True
        except Exception:
            return False
