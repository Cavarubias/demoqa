import pytest

@pytest.mark.smoke
def test_mark_1():
    assert True

@pytest.mark.regress
def test_mark_2():
    assert True

@pytest.mark.regress
def test_mark_3():
    assert True

@pytest.mark.regress
def test_mark_4():
    assert True


#    pytest tests/test_decor_mark.py -m smoke - запускает smoke тесты

#    pytest tests/test_decor_mark.py -m regress - запускает regress тесты

