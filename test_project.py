import pytest
from project import name_validator
from project import point_converter
from project import point_scored


"""
As some of this functions requiere input, please pass the following command:
-->     pytest -s test_project.py

When asked to put an input run:
- You are going to get reprompted unless you enter 2 valid names (less than 20 characters, no numbers)
- When asked: "Are you sure to exit? write "yes" or "no":" --> write "yes"
"""



def test_point_scored():
    assert point_scored("1") == (1, 0)
    assert point_scored("2") == (0, 1)

    with pytest.raises(ValueError):
        point_scored("3")

    with pytest.raises(SystemExit):
        point_scored("d")



def test_point_converter():
    assert point_converter([2, 1], tiebreak=0) == [30, 15]
    assert point_converter([4, 1], tiebreak=0) == ["Game 🏅", 0]
    assert point_converter([2, 4], tiebreak=0) == [0, "Game 🏅"]
    assert point_converter([3, 3], tiebreak=0) == ["40❕", "40❕"]
    assert point_converter([4, 3], tiebreak=0) == ["Adv❗", 40]
    assert point_converter([6, 4], tiebreak=1) == [6, 4]



def test_name_validator():
    assert name_validator("Rafa Nadal") == True

    with pytest.raises(ValueError, match="Name too long"):
        name_validator("Alejandro Davidovich Fokina")

    with pytest.raises(ValueError, match="Name cannot contain numbers"):
        name_validator("SerenaWilliams23")
  
