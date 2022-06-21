class Base1:

    var1a = 0

    var1b = 'a'

    def __init__(self):

        pass

    def func1a(self):

        print("fun1a from Base 1")

    def func1b(self):

        print("fun1b from Base 1")


class Base2:

    var2a = 1

    var2b = 'b'

    def __init__(self):

        pass

    def func2a(self):

        print("func2a from Base 2")

    def func2b(self):

        print("func2b from Base 2")


class Base3:

    var2a = 2

    var2b = 'c'

    def __init__(self):
        pass

    def func2a(self):
        print("func2a from Base 3")

    def func2b(self):
        print("func2b from Base 3")


# Case 1: Expected behavior
class Derived(Base1, Base2):

    def __init__(self):

        super(Derived, self).__init__()


# Case 2: Works but not really. Even though methods can be overridden. But unfortunately,
# the inherited properties are ambiguous. This type of inheritance is said to be incompatible.
class StrangeDerived(Base2, Base3):

    def __init__(self):

        super(StrangeDerived, self).__init__()

    def func2a(self):

        Base2.func2a(self)
        Base3.func2a(self)

    def func2b(self):

        Base2.func2b(self)
        Base3.func2b(self)


if __name__ == "__main__":

    D = Derived()

    print(D.var1a, D.var1b, D.var2a, D.var2b)

    D.func1a()
    D.func1b()
    D.func2a()
    D.func2b()

    print()

    SD = StrangeDerived()

    # Some information are lost in the StrangeDerived object.
    print(SD.var2a, SD.var2b)

    SD.func2a()
    SD.func2b()
