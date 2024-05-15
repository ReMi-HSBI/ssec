"""Module containing common utilities."""

from __future__ import annotations

import http
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import types
    from collections.abc import Iterator

    import httpx

from .constants import DELIMITER, SSE_CONTENT_TYPE
from .event import Event


def check_response(response: httpx.Response) -> None:
    """Check the response for errors.

    Parameters
    ----------
    response
        The response to check for errors.

    Raises
    ------
    ValueError
        If the response status code is invalid.
    TypeError
        If the response content type is invalid.
    """
    if response.status_code != http.HTTPStatus.OK:
        message = f"Unexpected status code: {response.status_code}!"
        raise ValueError(message)

    if SSE_CONTENT_TYPE not in response.headers.get("content-type"):
        message = f"Invalid content type: expected {SSE_CONTENT_TYPE}!"
        raise TypeError(message)


def extract_lines(buffer: str) -> tuple[list[str], str]:
    """Extract all lines from a string buffer.

    Parameters
    ----------
    buffer
        The buffer potentially containing lines.

    Returns
    -------
    tuple[list[str], str]
        A tuple containing extracted lines of the buffer as well as it's remnant.
    """
    lines: list[str] = []
    for line in buffer.splitlines(keepends=True):
        if line.endswith(("\r\n", "\n", "\r")):
            # Using '\r\n' as the parameter to rstrip means that it will strip
            # out any trailing combination of '\r' or '\n'.
            lines.append(line.rstrip("\r\n"))
            buffer = buffer.removeprefix(line)
    return lines, buffer


def parse_events(
    lines: list[str],
    external_config: types.SimpleNamespace,
) -> Iterator[Event]:
    """Parse server-sent events from a list of lines.

    Parameters
    ----------
    lines
        A list of lines to parse server-sent events from.
    external_config
        A configuration object containing the `last_event_id` and `reconnect_time`.
    """
    event_type = ""
    event_data = ""
    for line in lines:
        # If the line is empty (a blank line) -> Dispatch the event.
        if not line:
            if not event_type:
                event_type = "message"

            # Remove last character of data if it is a U+000A LINE FEED (LF) character.
            event_data = event_data.rstrip("\n")

            yield Event(event_type, event_data)
            continue

        # If the line starts with a U+003A COLON character (:) -> Ignore the line.
        if line.startswith(DELIMITER):
            continue

        name, _, value = line.partition(DELIMITER)

        # Space after the colon is ignored if present.
        value = value.removeprefix(" ")

        match name:
            case "event":
                # If the field name is "event"
                # -> Set the event type buffer to field value.
                event_type = value
            case "data":
                # If the field name is "data"
                # -> Append the field value to the data buffer, then append a
                # single U+000A LINE FEED (LF) character to the data buffer.
                event_data += f"{value}\n"
            case "id":
                # If the field name is "id"
                # -> If the field value does not contain U+0000 NULL, then set
                # the last event ID buffer to the field value. Otherwise,
                # ignore the field. The specification is not clear here.
                # In an example it says: "If the "id" field has no value, this
                # will reset the last event ID to the empty string"
                external_config.last_event_id = value
            case "retry":
                # If the field name is "retry"
                # -> If the field value consists of only ASCII digits, then
                # interpret the field value as an integer in base ten, and set
                # the event stream's reconnection time to that integer.
                # Otherwise, ignore the field.
                if value.isdigit():
                    external_config.reconnection_time = int(value)
            case _:
                # Otherwise -> The field is ignored.
                continue
