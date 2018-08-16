class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()

this = obj.method()
print(this)
this=obj.classmethod()
print(this)
this=obj.staticmethod()
print(this)

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

this=Pizza(['chicken','bbq sauce','onions','bacon'])
for i in this.ingredients:
    print(i)
print(this)
print(Pizza.margherita())

print(Pizza.prosciutto())