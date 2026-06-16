from typing import IO, Iterable

import json5


def load(fp: IO, **kwargs):
    """
    Deserialize ``fp`` (a ``.read()``-supporting file-like object
    containing a JSONL5 document) to a Python object.

    Supports the same arguments as :func:`json5.load`
    """
    s = fp.read()
    return loads(s, **kwargs)


def loads(s: str, **kwargs) -> list:
    """
    Deserialize ``s`` (a string containing a JSONL5 document) to a Python object.

    Supports the same arguments as :func:`json5.loads`
    """
    output = []
    for i, line in enumerate(s.splitlines()):
        line = line.strip()
        if not line:
            continue
        
        try:
            output.append(json5.loads(line, **kwargs))
        except ValueError as e:
            raise ValueError(
                f"Error parsing line {i + 1}: {line}"
            ) from e
    
    return output

    # return [json5.loads(s, **kwargs) for s in s.splitlines() if s.strip()]



def dump(obj: Iterable, fp: IO, **kwargs):
    """
    Serialize ``obj`` to a JSONL5-formatted stream to ``fp``,
    a ``.write()``-supporting file-like object.

    Supports the same arguments as :func:`json5.dump`
    """
    fp.write(dumps(obj, **kwargs))


def dumps(obj: Iterable, **kwargs):
    """
    Serialize ``obj`` to a JSONL5-formatted string.

    Supports the same arguments as :func:`json5.dumps`
    """
    return "\n".join(json5.dumps(item, **kwargs) for item in obj)
