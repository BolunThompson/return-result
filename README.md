[![PyPI version](https://img.shields.io/pypi/v/return-result)](https://pypi.org/project/return-result/)
[![Python versions](https://img.shields.io/pypi/pyversions/return-result.svg)](https://pypi.org/project/return-result/)
[![Black codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# return-result

*I am not maintaining this; it likely will not work and has bugs.*

This defines a decorator that causes the variable `result` to be automatically returned from a function when there is no return statement. 

This works by getting the source code of the decorated function, so this won't work in the CPython REPL. It does work in IPython however.

Inspired by the [Nim feature](https://nim-by-example.github.io/variables/result/) that does the same thing.


# Example

```python
>>> from return_result import return_result
>>> @return_result
... def test():
...     result = "Works!"
>>> test()
'Works!'
```

# Requirements

Python 3.6+
