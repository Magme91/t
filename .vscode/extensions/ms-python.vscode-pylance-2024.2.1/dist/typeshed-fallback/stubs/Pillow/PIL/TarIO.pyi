from types import TracebackType
from typing_extensions import Self

from .ContainerIO import ContainerIO

class TarIO(ContainerIO[bytes]):
    def __init__(self, tarfile: str, file: str) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def close(self) -> None: ...
