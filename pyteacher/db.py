import os

import pandas as pd


class PyTeacherDB:
    def __init__(self, files_dir=".files"):
        path_users = files_dir + "/users.csv"
        if os.path.exists(path_users):
            self.users = pd.read_csv(path_users)
        else:
            self.users = pd.DataFrame(list())
