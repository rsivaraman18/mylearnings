class Phone:
    def set_color(self,color):
        self.color=color
        print("set_color")

    def set_cost(self,cost):
        self.cost=cost
        print('color')

    def show_color(self):
        return self.color
    
    def show_cost(self):
        return self.cost

key = Phone()
key.set_color('green')
print(key.show_color())

