import typing
from typing import Protocol, TypedDict

import mypy_extensions
import typing_extensions
from typing_extensions import Literal, TypeAlias

class _Foo(Protocol):  # Y046 Protocol "_Foo" is not used
    bar: int

class _Bar(typing.Protocol):  # Y046 Protocol "_Bar" is not used
    bar: int

class _Baz(typing_extensions.Protocol):  # Y046 Protocol "_Baz" is not used  # Y023 Use "typing.Protocol" instead of "typing_extensions.Protocol"
    bar: int

class UnusedButPublicProtocol(Protocol):
    bar: int

class _UsedPrivateProtocol(Protocol):
    bar: int

def uses__UsedPrivateProtocol(arg: _UsedPrivateProtocol) -> None: ...

_UnusedPrivateAlias: TypeAlias = str | int  # Y047 Type alias "_UnusedPrivateAlias" is not used
PublicAlias: TypeAlias = str | int
_UsedAlias: TypeAlias = Literal["Look, this is used!"]

def uses__UsedAlias(arg: _UsedAlias) -> None: ...

class _UnusedTypedDict(TypedDict):  # Y049 TypedDict "_UnusedTypedDict" is not used
    foo: str

class _UnusedTypedDict2(typing_extensions.TypedDict):  # Y049 TypedDict "_UnusedTypedDict2" is not used
    bar: int

class _UnusedTypedDict3(mypy_extensions.TypedDict):  # Y049 TypedDict "_UnusedTypedDict3" is not used
    baz: dict[str, str]

class _UsedTypedDict(TypedDict):
    baz: bytes

class _Uses_UsedTypedDict(_UsedTypedDict):
    spam: list[int]

class _UsedTypedDict2(TypedDict):
    ham: set[int]

def uses__UsedTypeDict2(arg: _UsedTypedDict2) -> None: ...

_UnusedTypedDict4 = TypedDict("_UnusedTypedDict4", {"-": int, "def": str})  # Y049 TypedDict "_UnusedTypedDict4" is not used
_UnusedTypedDict5 = typing_extensions.TypedDict("_UnusedTypedDict5", {"foo": bytes, "bar": str})  # Y049 TypedDict "_UnusedTypedDict5" is not used  # Y031 Use class-based syntax for TypedDicts where possible
_UsedTypedDict3 = mypy_extensions.TypedDict("_UsedTypedDict3", {".": list[int]})

uses__UsedTypedDict3: _UsedTypedDict3

class UnusedButPublicTypedDict(TypedDict):
    foo: str

UnusedButPublicTypedDict2 = TypedDict("UnusedButPublicTypedDict", {"99999": frozenset[str]})
