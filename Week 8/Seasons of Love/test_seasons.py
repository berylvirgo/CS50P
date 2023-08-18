from seasons import convert_to_words, get_dob


def test_convert_to_words():
    # Test 1: Today is 2032-01-01
    assert convert_to_words("2012-01-02") == "Six million, eighty-nine thousand, seven hundred sixty minutes"

    # Test 2: Today is 2023-07-30
    assert convert_to_words("1993-09-24") == "Fifteen million, seven hundred thousand, three hundred twenty minutes"

    # Test 3: Today is 2023-07-30
    assert convert_to_words("1996-01-02") == "Fourteen million, five hundred five thousand, one hundred twenty minutes"

    # Test 4: Today is 2023-07-30
    assert convert_to_words("1970-01-03") == "Twenty-eight million, one hundred seventy-seven thousand, nine hundred twenty minutes"

    # Test 5: Today is 2023-07-30
    assert convert_to_words("2023-07-03") == "Forty-one thousand, seven hundred sixty minutes"


def test_get_dob():
    # Test 1: Valid date in the correct format
    assert get_dob("2023-07-30") == "2023-07-30"

    # Test 2: Date with incorrect format - should raise SystemExit
    with pytest.raises(SystemExit):
        get_dob("07-30-2023")

    # Test 3: Invalid date - should raise SystemExit
    with pytest.raises(SystemExit):
        get_dob("January 1, 1999")

    # Test 5: Empty input - should raise SystemExit
    with pytest.raises(SystemExit):
        get_dob("")