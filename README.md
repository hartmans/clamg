# CLassAttributeModelGenerator

Given a [YAML](https://yaml.org) file; create a hierarchical object model.

Some would say this is just a dict-wrapper.

### Example

```yaml
    obj:
      attr1:
        - item1
        - item2
        - item3
      attr2:
        sub_attr_a: '42'
        sub_attr_b: 'foo'
```

Will result in the following structure:

```python3
    <(obj=<obj(attr1=['item1', 'item2', 'item3'], attr2=<attr2(sub_attr_a=42, sub_attr_b=foo)>)>)>
```

It has occasionally proven useful when interacting with REST APIs.
