import contextlib
import logging

import ssec


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    with contextlib.suppress(KeyboardInterrupt):
        for event in ssec.sse(
            "https://stream.wikimedia.org/v2/stream/recentchange",
        ):
            print(event)


main()
