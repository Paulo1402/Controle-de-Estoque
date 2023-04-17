class Foo:
    def __init__(self, name):
        self.name = name


class Bar(Foo):
    def __init__(self, name):
        super().__init__(name)


bar = Bar('bar')
print(bar.name)
