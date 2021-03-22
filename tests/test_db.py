from pyteacher.db import PyTeacherDB
from pyteacher.models import User


def test_db():
    user_1 = User(telegram_user_id="1")
    with PyTeacherDB(db="dev_db") as db:
        assert db.add_user(user_1)
        assert not db.add_user(user_1)
        assert db.remove_user(user_1.telegram_user_id)
        db._mongo.drop_database("dev")  # pylint: disable=protected-access
