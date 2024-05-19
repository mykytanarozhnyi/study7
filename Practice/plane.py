class Plane:

    def __init__(self,make,model,year,capacity,destroyed):
        self.make = make
        self.model = model
        self.year = year
        self.capacity = capacity
        self.isdestroyed = destroyed

    def fly(self):
        print("This "+self.make+" is flying")

    def stop(self):
        print("This "+self.make+" is drowned")

    def destroyed(self):
        print("This "+self.model+" is destroyed")