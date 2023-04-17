from abc import ABC, ABCMeta, abstractmethod

from PySide6.QtCore import QObject, QRegularExpression, QMetaObject, QMetaType
from PySide6.QtGui import QRegularExpressionValidator


class Meta(ABCMeta, type(QObject)):
    pass


class Abstract(ABC, metaclass=Meta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def fixup(self, arg__1: str) -> str:
        print('superclass')


class Foo(Abstract):
    def __init__(self):
        super().__init__()

    def fixup(self, arg__1: str) -> str:
        print(arg__1)


class Bar(Abstract):
    def __init__(self):
        super().__init__()

    def fixup(self, arg__1: str) -> str:
        print(arg__1)


foo = Foo()
foo.fixup('foo')

bar = Bar()
bar.fixup('bar')

# print(isinstance(foo, (Foo, Bar)))
# print(isinstance(bar, (Foo, Bar)))

a = Abstract()
a.fixup('a')
