# aiosse

[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

## Description

Yet another asynchronous library for server-sent events.  
This library works with [aiohttp](https://docs.aiohttp.org/en/stable).

## Note
Although there are already some libraries on the subject
([aiohttp-sse-client](https://github.com/rtfol/aiohttp-sse-client),
[aiosseclient](https://github.com/ebraminio/aiosseclient)), these are
unfortunately not entirely correct. In example, both asynchronously iterate
over the stream content via `async for line in response.content`[^1][^2].
This internally calls [aiohttp](https://docs.aiohttp.org/en/stable)'s [`readuntil`](https://docs.aiohttp.org/en/stable/streams.html#aiohttp.StreamReader.readuntil) method with
the default seperator `\n`, but the official specification says:

> Lines must be separated by either a U+000D CARRIAGE RETURN U+000A LINE FEED
   (CRLF) character pair, a single U+000A LINE FEED (LF) character, or a
   single +000D CARRIAGE RETURN (CR) character.

Another point is the error handling, which is often not sufficient to analyze
the error or is entirely skipped.

[^1]: [Code Reference](https://github.com/rtfol/aiohttp-sse-client/blob/e311075ac8b9b75d8b09512f8638f1dd03e2ef2b/aiohttp_sse_client/client.py#L157)   
[^2]: [Code Reference](https://github.com/ebraminio/aiosseclient/blob/375d597bcc3a7bf871b65913b366d515b300dc93/aiosseclient.py#L131)

## Installation

aiosse is written in [Python](https://www.python.org) and tries to keep track
of the newest version available. Currently[^3], this is
[Python 3.12.3](https://www.python.org/downloads/release/python-3123/).
On some operating systems, this version is pre-installed, but on many it is
not. This guide will not go into details on the installation process, but
there are tons of instructions out there to guide you. A good starting point
is the [beginners guide](https://www.python.org/about/gettingstarted/).

[^3]: 06\. May 2024

## Installation (User)

There is no user installation yet. Please refer to the developer installation.

## Installation (Developer)

1\. Clone this repository to a desired location on your maschine using `ssh`:

```sh
git git@github.com:sharly-project/aiosse.git
```

2\. Change into the project directory:

```sh
cd aiosse
```

3\. Create a virtual environment:

```sh
python -m venv .venv
```

> Depending on the installation `python` may deviate e.g. `py` on Windows or
> `python3.12` on Linux.

4\. Activate the virtual environment:

**Windows**:

```sh
 .\.venv\Scripts\activate
```

**Linux**:

```sh
 source \.venv\bin\activate
```

**MacOS**:

```sh
-
```

> If everything worked out, you should now see a **(.venv)** prompt in your
> terminal.

5\. Install aiosse's developer edition:

```sh
pip install --editable .[dev]
```
