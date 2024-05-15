"""Module containing constant values."""

from __future__ import annotations

import codecs
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

DEFAULT_CONNECT_TIMEOUT: Final[float] = 3.0
#: The default timeout for connecting to a server, in seconds.

DEFAULT_CHUNK_SIZE: Final[int] = 1024
#: The default chunk size for streaming server-sent events, in bytes.

DEFAULT_MAX_CONNECT_ATTEMPTS: Final[int] = 3
#: The default maximum number of attempts to connect to a server.

DEFAULT_RECONNECT_TIMEOUT: Final[float] = 3.0
#: The default time to wait before reconnecting to a server, in seconds.

DEFAULT_BACKOFF_DELAY: Final[float] = 2.5
#: The default additional time to wait to ease a potentially overloaded server, in seconds.  # noqa: E501

DECODER = codecs.getincrementaldecoder("utf-8")(errors="replace")
#: The incremental UTF-8 decoder with replacement error handling.

DELIMITER: Final[str] = ":"
#: The delimiter used in server-sent events.

SSE_CONTENT_TYPE: Final[str] = "text/event-stream"
SSE_CACHE_CONTROL: Final[str] = "no-store"

HEADERS: Final[dict[str, str]] = {
    "Accept": SSE_CONTENT_TYPE,
    "Cache-Control": SSE_CACHE_CONTROL,
}