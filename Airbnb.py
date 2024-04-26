class Rental:
    def __init__(self,name,meters,price):
        self.name = name
        self.meters = meters
        self.price = price
    def print(self):
        print(f"This is {self.name} has {self.meters} meters, and costs {self.price}")
if __name__ == "__main__":
    flat = Rental("Amazing flat","58","1000$")

print (Rental)
flat.print()