from typing import Protocol


class P(Protocol):
    def method1(self, arg: int) -> None: ...  # Y058 Argument "arg" to protocol method "method1" should not be positional-or-keyword (suggestion: make it positional-only)
    def method2(self, arg: str, /) -> None: ...
    def method3(self, *, arg: str) -> None: ...