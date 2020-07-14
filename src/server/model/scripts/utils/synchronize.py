import asyncio
import functools
from typing import Any, Awaitable, Callable

AsyncCallable = Callable[..., Awaitable[Any]]


def synchronize(semaphore: asyncio.Semaphore, /) -> Callable[[AsyncCallable], AsyncCallable]:
    def acquire(func: AsyncCallable, /) -> AsyncCallable:
        @functools.wraps(func)
        async def wrap(*args, **kwargs):
            async with semaphore:
                return await func(*args, **kwargs)
        return wrap
    return acquire
