class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        properties = ""
        for item in vars(self).values():
            properties += f", {repr(item)}"
        return f"{self.__class__.__name__}({properties[2:]})"
