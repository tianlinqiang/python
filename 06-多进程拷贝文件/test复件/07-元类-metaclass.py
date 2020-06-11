def upper_attr(fun_class_name,fun_class_parents,fun_class_attr):
    newAttr = {}
    for name,value in fun_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
    return type(fun_class_name, fun_class_parents, newAttr)

class Foo(object):
    __metaclass__ = upper_attr
    bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

t = Foo()
print(t.BAR)
print(t.bar)
