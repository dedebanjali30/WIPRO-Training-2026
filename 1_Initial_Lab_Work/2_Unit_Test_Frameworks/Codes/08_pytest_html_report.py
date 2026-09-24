def test_login():
    username = "admin"
    password = "admin123"

    assert username == "admin"
    assert password == "admin123"


def test_title():
    title = "Automation Practice"

    assert "Automation" in title