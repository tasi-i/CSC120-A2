class ResaleShop:
    profit:float
    inventory:str
    
    def __init__(self):
        self.inventory=[]
        self.profit=0.0
        


    def buy_computer(self, computer):
        self.inventory.append(computer)

    def sell_computer(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            self.profit+=computer.price
        else:
            print("Error: The computer is not found in inventory")
