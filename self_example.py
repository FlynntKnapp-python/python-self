class Container:
    def __init__(self, name):
        self.name = name


class Box(Container):
    def __init__(self_in_different_class, name):
        super().__init__(name)
