class Pizza:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class PizzaPan(Pizza):
    cost = 0.0

class Ingredients(Pizza):
    def __init__(self, Pizza):
        self.component = Pizza
    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription()+ ' ' + Pizza.getDescription(self)

class Cheese(Ingredients):
    cost = 0.75
    def __init__(self, Pizza):
        Ingredients.__init__(self, Pizza)

class Pepperoni(Ingredients):
    cost = 0.75
    def __init__(self, Pizza):
        Ingredients.__init__(self, Pizza)

class Tomato(Ingredients):
    cost = 0.25
    def __init__(self, Pizza):
        Ingredients.__init__(self, Pizza)

class Basil(Ingredients):
    cost = 0.25
    def __init__(self, Pizza):
        Ingredients.__init__(self, Pizza)

class TomatoPulp(Ingredients):
    cost = 1.00
    def __init__(self, Pizza):
        Ingredients.__init__(self, Pizza)

class Chocolate(Ingredients):
    cost = 1.00
    def __init__(self, Pizza):
       Ingredients.__init__(self, Pizza)

if __name__ == "__main__":
    margherita = Cheese(Tomato(TomatoPulp(Basil(PizzaPan()))))
    print(margherita.getDescription()+ ": $" + str(margherita.getTotalCost()))

    chocolate = Chocolate(PizzaPan())
    print(chocolate.getDescription()+ ": $" + str(chocolate.getTotalCost()))

    pepperoni = Pepperoni(TomatoPulp(Cheese(PizzaPan())))
    print(pepperoni.getDescription()+ ": $" + str(pepperoni.getTotalCost()))