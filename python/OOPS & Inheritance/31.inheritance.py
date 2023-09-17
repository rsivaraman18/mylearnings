class Parent:
    def assign_name(self,name):
        self.name = name

    def show_name(self):
        return self.name

class Child(Parent):
    def assign_age(self,age):
        self.age =age

    def show_age(self):
        return self.age

class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender =gender

    def show_gender(self):
        return self.gender

key =GrandChild()
key.assign_name('siva')
key.assign_age(10)
key.assign_gender('male')
print(key.show_name())
print(key.show_age())
print(key.show_gender())

