from abc import ABC, abstractmethod
from typing import Self


class AbstractUnitOfWork(ABC):
    def __init__(self, auto_commit: bool = True):
        self._auto_commit = auto_commit

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._auto_commit:
            await self.commit()
        if exc_type:
            await self.rollback()

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
