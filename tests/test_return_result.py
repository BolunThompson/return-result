from return_result import return_result
import pytest


@return_result
def func_test_result():
    result = "works"


@return_result
def func_test_explicit_return():
    result = "doesn't work"
    return "works"


@return_result
def func_test_no_result():
    return "works"


@pytest.mark.parametrize(
    "func", [func_test_result, func_test_explicit_return, func_test_no_result]
)
def test_return_result(func):
    assert func() == "works"
