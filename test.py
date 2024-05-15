import logging

import ssec


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    for event in ssec.stream("https://stream.wikimedia.org/v2/stream/recentchange"):
        print(event)


main()
