from um import count

def test_single_count():
    # Test with single occurrence of "um" as a word
    assert count("hello, um, world") == 1


def test_no_count():
    # Test with no occurrence of "um" as a word
    assert count("yummy") == 0

    # Test with numbers and symbols (should not count)
    assert count("The sum of 5 and 7 is 12.") == 0


def test_multiple_count():
    # Test with multiple occurrences of "um" as a word
    assert count("Um, um, uM, UM") == 4

    # Test with uppercase and lowercase characters mixed
    assert count("uM uM uM") == 3


def test_substring_count():
    # Test with word "umlaut" containing "um" as a substring (should not count)
    assert count("The word umlaut has um in it.") == 1