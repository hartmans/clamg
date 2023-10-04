import json
import io
import os
import yaml

__version__ = 0.3

__all__ = []

class Base:
    def __init__(self, *args, **kwargs):
        for a in args:
            if type(a) is dict:
                self.__dict__ = a
        for k, v in kwargs.items():
            if k in allkw:
                self.__dict__.update({k:v})

    def __getitem__(self, key):
        return self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __repr__(self):
        items = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(items)})>"


def loads(s: str, _yaml=True, _json=False) -> Base:
    """A string that should be decoded
    """
    if _yaml:
        data = yaml.safe_load(s)
    elif _json:
        data = json.loads(s)

    return unpack(data)

__all__ += ["loads"]


def load(fp: str | os.PathLike | io.TextIOWrapper, _yaml=True, _json=False) -> Base:
    """
        Args:
            fp: will be normalized to a filelike object and read from.
        Returns:
            clamg.Base
    """
    fh = None

    if isinstance(fp, str):
        fh = open(fp)
    elif isinstance(fp, io.TextIOWrapper):
        fh = fp
    elif isinstance(fp, os.PathLike):
        fh = fp.open()

    if _yaml:
        data = yaml.safe_load(fh.read())
    elif _json:
        data = json.loads(fh.read())

    return unpack(data)

__all__ += ["load"]


def unpack(i: object, rk='clamg'):
    """Return a class-attribute model from data

        Args:
            i: A primitive type like dict, list, str ...

        Returns:
            clamg.Base
    """
    attrs = {}
    if type(i) is dict:
        for k, v in i.items():
            if type(v) is dict:
                attrs.update({k:unpack(v, k)})
            elif (
                (type(v) is list)
                or (type(v) is tuple)
                or (type(v) is set)
            ):
                attrs.update({k:unpack(v, k)})
            elif (
                (type(v) is str)
                or (type(v) is int)
                or (type(v) is bool)
                or (type(v) is float)
            ):
                attrs.update({k:v})
            else:
                raise ValueError(f"Unexpected type {type(v)}")
    elif type(i) is list:
        attrs = []
        for li in i:
            if type(li) is dict:
                attrs.append(unpack(li, rk))
            elif (
                (type(li) is list)
                or (type(li) is tuple)
                or (type(li) is set)
            ):
                attrs.append(unpack(li, rk))
            elif (
                (type(li) is str)
                or (type(li) is int)
                or (type(li) is bool)
                or (type(li) is float)
            ):
                attrs.append(li)
            else:
                raise ValueError(f"Unexpected type {type(li)}")
        return attrs
    elif (
        (type(i) is str)
        or (type(i) is int)
        or (type(i) is bool)
        or (type(i) is float)
    ):
        return i
    else:
        raise ValueError(f"Unexpected type {type(i)}")
    return type(rk[:-1] if rk.endswith('s') else rk, (Base,), {})(attrs)

__all__ += ["unpack"]
