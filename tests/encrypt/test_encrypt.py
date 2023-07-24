from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Test regular cases with valid inputs
    assert encrypt_message("HelloWorld", 3) == "leH_dlroWol"
    assert encrypt_message("AnotherExample", 5) == "htonA_elpmaxEre"
    assert encrypt_message("PythonIsCool", 1) == "P_looCsInohty"

    # Test cases with even/odd key
    assert encrypt_message("HelloWorld", 4) == "dlroWo_lleH"
    assert encrypt_message("DataScience", 7) == "icSataD_ecne"

    # Test case with key = 0
    assert encrypt_message("Hi", 0) == "iH"

    # Test case with key out of range
    assert encrypt_message("HelloWorld", 15) == "dlroWolleH"

    # Test case with key not an integer
    with pytest.raises(TypeError):
        encrypt_message("HelloWorld", 6.2)

    # Test case with message not a string
    with pytest.raises(TypeError):
        encrypt_message(999, 5)
