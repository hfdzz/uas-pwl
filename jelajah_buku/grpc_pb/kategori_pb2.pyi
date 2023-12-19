from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KategoriRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KategoriResponse(_message.Message):
    __slots__ = ("kategori", "text")
    KATEGORI_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    kategori: str
    text: str
    def __init__(self, kategori: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
