from twttr import shorten


def test_shorten():
    assert shorten("cat") == "ct"
    assert shorten("twitter") == "twttr"
    assert shorten("APPLE") == "PPL"
    assert shorten("Twitt3r") == "Twtt3r"
    assert shorten("pr,@oud!") == "pr,@d!"