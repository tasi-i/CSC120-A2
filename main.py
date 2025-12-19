# Main script for the Resale Shop project.
# Creates instances of Computer and ResaleShop.
# Adds computers to the shop inventory.
# Updates prices and operating systems as needed.
# Refurbishes computers to adjust their prices.
# Sells computers and updates the shop's profit.
# Prints inventory and profit at each stage.
from computer import Computer
from oo_resale_shop import ResaleShop

shop = ResaleShop()

# Create computers /inventory
comp1 = Computer("MacBook Pro", "M1", "512GB", "16GB", "macOS Monterey", 2021, 700)
comp2 = Computer("Dell XPS", "Intel i7", "1TB", "32GB", "Windows 10", 2015, 600)
comp3 = Computer("HP Pavilion", "Intel i5", "256GB", "8GB", "Windows 8", 2009, 100)

# Buy computers (add to inventory)
shop.buy_computer(comp1)
shop.buy_computer(comp2)
shop.buy_computer(comp3)

# inventory after buying
print("Inventory after buying:")
for comp in shop.inventory:
    print(f"{comp.description}, {comp.processor_type}, {comp.memory}, {comp.operating_system}, {comp.year_made}, ${comp.price}")

# Update price of comp2
comp2.update_price(750)

# Update OS of comp3
comp3.update_os("Windows 10")

# Refurbish comp3 and comp1
comp3.refurbish()
comp1.refurbish()

# Print inventory after updates
print("\n Inventory after updates:")
for comp in shop.inventory:
    print(f"{comp.description}, {comp.processor_type}, {comp.memory}, {comp.operating_system}, {comp.year_made}, ${comp.price}")

# Sell comp1
shop.sell_computer(comp1)

# inventory after selling
print("\n Inventory after selling one computer:")
for comp in shop.inventory:
    print(f"{comp.description}, {comp.processor_type}, {comp.memory}, {comp.operating_system}, {comp.year_made}, ${comp.price}")

# Print final profit
print(f"\n Total profit from sales: ${shop.profit}")
