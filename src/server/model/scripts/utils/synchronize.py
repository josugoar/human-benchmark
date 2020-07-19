import asyncio
import functools
from typing import Any, Awaitable, Callable, TypeVar

T = TypeVar("T")

AsyncCallable = Callable[..., Awaitable[T]]


def synchronize(lock: asyncio.locks._ContextManagerMixin, /) -> Callable[[AsyncCallable], AsyncCallable]:
    def acquire(func: AsyncCallable, /) -> AsyncCallable:
        @functools.wraps(func)
        async def wrap(*args: Any, **kwargs: Any):
            async with lock:
                return await func(*args, **kwargs)
        return wrap
    return acquire
