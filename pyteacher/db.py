import os

import pandas as pd

from pyteacher.models import User


class PyTeacherDB:
    def __init__(self, files_dir=".files"):
        path_users = files_dir + "/users.csv"
        if os.path.exists(path_users):
            self.users = pd.read_csv(path_users)
        else:
            self.users = pd.DataFrame(
                list(),
                columns=User.schema()["properties"].keys(),
            )

    def get_user(self, telegram_user_id):
        if telegram_user_id in self.users["telegram_user_id"]:
            users = self.users[self.users["telegram_user_id"] == telegram_user_id]
            return users.iloc[0]
        return None

    def exists_user(self, telegram_user_id):
        return self.get_user(telegram_user_id) is not None

    def add_user(self, user):
        try:
            self.users = self.users.append(user.dict(), ignore_index=True)
            return True
        except Exception:
            return False

    def remove_user(self, telegram_user_id):
        try:
            target_indices = self.users[
                self.users["telegram_user_id"] == telegram_user_id
            ].index
            self.users.drop(target_indices, inplace=True)
            return True
        except Exception:
            return False
