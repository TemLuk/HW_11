class A:
    def __init__(self):
        self.cat = "Murzik"

    @property
    def get_locals(self):
        return locals()


a = A()
print(a.get_locals)
