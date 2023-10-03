# CLassAttributeModelGenerator

Given a [YAML](https://yaml.org) file or a [JSON](https://www.json.org) structure create a hierarchical object model.

Some would say this is just a dict-wrapper.

### Example 1

```python3

    >>> a = '''obj:
    ...   obj_list:
    ...     - 1
    ...     - 2
    ...     - dog
    ...   obj_dict:
    ...     key_foo: bar
    ...     key_spam: eggs
    ... '''
    >>> b = clamg.loads(a)
    >>> b.obj
    <obj(obj_list=[1, 2, 'dog'], obj_dict=<obj_dict(key_foo=bar, key_spam=eggs)>)>

```

### Example 2

```python3

    >>> j = '''{
    ...     "obj": {
    ...         "obj_list": [
    ...             1, 2, "dog"
    ...         ],
    ...         "obj_dict": {
    ...             "key_foo":"bar",
    ...             "key_spam":"eggs"
    ...         }
    ...     }
    ... }'''
    >>> jl = json.loads(j)
    >>> h = clamg.unpack(jl)
    >>> h
    <(obj=<obj(obj_list=[1, 2, 'dog'], obj_dict=<obj_dict(key_foo=bar, key_spam=eggs)>)>)>

```

It has occasionally proven useful when working with deeply nested structures.
