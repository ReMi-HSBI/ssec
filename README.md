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

**1\. Clone this repository to a desired location on your maschine using `ssh`:**

```sh
git git@github.com:sharly-project/aiosse.git
```

**2\. Change into the project directory:**

```sh
cd aiosse
```

**3\. Create a virtual environment:**

..with [`venv`](https://docs.python.org/3/library/venv.html):
```sh
python3.12 -m venv .venv
```

..with [`uv`](https://github.com/astral-sh/uv):
```sh
uv venv -p 3.12
```

**4\. Activate the virtual environment:**

.. on Windows:
```sh
 .\.venv\Scripts\activate
```

.. on Linux:
```sh
 source \.venv\bin\activate
```

.. on MacOS:
```sh
-
```

> If everything worked out, you should now see a **(.venv)** or **(aiosse)** 
> prompt in your terminal.

**5\. Install aiosse's developer edition:**

..with [`pip`](https://pip.pypa.io/en/stable):
```sh
pip install -e .[dev]
```

..via [`uv`](https://github.com/astral-sh/uv):
```sh
uv pip install -e .[dev]
```

## Miscellaneous

### Documentation

Build the documentation by running the following command in the root directory
of the project:

```sh
sphinx-build -b html docs/src docs/build
```

> The command requires that the [developers edition](#installation-developer)
> of `aiosse` is installed and the virtual environment is running.

The documentation is then accessible via `doc/build/index.html`.

### Set up Visual Studio Code for Development

To edit the code base with [Visual Studio Code](https://code.visualstudio.com),
install the following extensions:

| Name              | URL                                                                                  |
|-------------------|--------------------------------------------------------------------------------------|
| Python            | <https://marketplace.visualstudio.com/items?itemName=ms-python.python>               |
| Mypy Type Checker | <https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker>    |
| Ruff              | <https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff>             |
| markdownlint      | <https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint> |
| Even Better TOML  | <https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml>       |

Necessary settings are already included in the `.vscode` directory and should
be enabled per default.

## Contributing

Contributing to `aiosse` is highly appreciated, but comes with some requirements:

1. **Type Hints**

    Write modern python code using
    [type annotations](https://peps.python.org/pep-0484/)
    to enable static analysis and potential runtime type checking.

2. **Documentation**

    Write quality documentation using
    [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
    docstring conventions.

3. **Linting**

   Lint your code with [ruff](https://github.com/charliermarsh/ruff) and
   [mypy](http://mypy-lang.org).

4. **Style**

    Format your code using [ruff](https://github.com/charliermarsh/ruff).

5. **Testing**

    Write tests for your code using
    [unittest](https://docs.python.org/3/library/unittest.html).