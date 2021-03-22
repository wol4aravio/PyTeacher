from pyteacher.bot_tools import parse_register_message


def test_parse_register_message_1():
    assert parse_register_message("/register") is None


def test_parse_register_message_2():
    url = "https://github.com/wol4aravio/PyTeacher"
    assert parse_register_message("/register {}".format(url)) == url
