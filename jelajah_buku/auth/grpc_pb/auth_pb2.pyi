from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Credential(_message.Message):
    __slots__ = ("email", "password", "token")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    token: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class UserData(_message.Message):
    __slots__ = ("id", "email", "nama")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    id: int
    email: str
    nama: str
    def __init__(self, id: _Optional[int] = ..., email: _Optional[str] = ..., nama: _Optional[str] = ...) -> None: ...

class UserID(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class IsAuth(_message.Message):
    __slots__ = ("isAuth", "id")
    ISAUTH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    isAuth: bool
    id: int
    def __init__(self, isAuth: bool = ..., id: _Optional[int] = ...) -> None: ...
