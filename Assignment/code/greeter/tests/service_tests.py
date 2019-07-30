from greeter.services import greeting


def test_greeting_no_paramter():
    # force pr
    assert greeting() == "Hello Moneyflow!!"


def test_greeting_en():
    assert greeting("en") == "Hello Moneyflow!!"


def test_greeting_da():
    assert greeting("da") == "Hej Moneyflow!!"
