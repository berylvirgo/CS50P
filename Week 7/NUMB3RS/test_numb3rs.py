from numb3rs import validate, matches


def test_validate_valid_numbers():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_validate_invalid_numbers():
    assert validate("275.275.275.275") == False
    assert validate("255.275.0.1") == False


def test_validate_letters():
    assert validate("cat") == False


def test_matches():
    assert matches("127.0.0.1") == "127.0.0.1"
    assert matches("1.2.3.1000") == "1.2.3.1000"
    assert matches("cat") == None