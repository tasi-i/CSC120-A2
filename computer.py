#Computer class for the Resale Shop project.
#Represents a computer with attributes such as description, processor type,
#hard drive capacity, memory, operating system, year made, and price.
#Includes methods to update price, update operating system, and refurbish the computer.
class Computer:
#all characteristics of cpmputer
    def __init__(self,description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):

     self.description = description
     self.processor_type = processor_type
     self.hard_drive_capacity = hard_drive_capacity
     self.memory = memory
     self.operating_system = operating_system
     self.year_made = year_made
     self.price=price
     

#updating the price of the computer
    def update_price(self, new_price):
       self.price = new_price

    def update_os(self, new_os):
       self.operating_system = new_os
#refurbish price
    def refurbish(self):
       if self.year_made < 2000:
          self.price = 1
       elif self.year_made <2010:
          self.price=251
       elif self.year_made <2018:
          self.price=550
       else: 
          self.price=891

