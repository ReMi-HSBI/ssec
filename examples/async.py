import asyncio
import contextlib
import logging

import ssec


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    with contextlib.suppress(asyncio.CancelledError):
        async for event in ssec.sse_async(
            "https://stream.wikimedia.org/v2/stream/recentchange",
        ):
            print(event)


asyncio.run(main())
