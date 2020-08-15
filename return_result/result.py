import ast
import inspect
import typing as tp

T = tp.TypeVar("T", bound=tp.Callable)


def return_result(func: T) -> T:
    """
    Decorator to automatically return the `result` variable if there is no return

    This is a function decorator that returns the result variable if
    the function wasn't explicitly returned. An empty return statement
    still returns None.

    >>> @return_result
    ... def test():
    ...     result = "Works!"
    >>> test()
    'Works!'
    """
    try:
        source = inspect.getsource(func)
    except OSError as e:
        raise ValueError(f"Cannot get the source code of {func}") from e
    file = inspect.getfile(func)

    source_module_ast = ast.parse(source)
    source_func_ast = tp.cast(ast.FunctionDef, source_module_ast.body[0])

    try_return_source = """
try:
    return result
except NameError:
    pass
"""

    try_return_ast = ast.parse(try_return_source, file).body[0]

    source_func_ast.body.append(try_return_ast)
    source_func_ast.decorator_list.clear()

    compiled_source = compile(source_module_ast, filename=file, mode="exec")
    namespace: tp.Dict[str, tp.Any] = {}
    exec(compiled_source, namespace)
    return namespace[func.__name__]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
