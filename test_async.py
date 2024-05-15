import asyncio
import logging

import ssec


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    async for event in ssec.stream_async(
        "https://stream.wikimedia.org/v2/stream/recentchange",
    ):
        print(event)


asyncio.run(main())
