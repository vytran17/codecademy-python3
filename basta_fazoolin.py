"""Restaurant franchise business"""

class Menu:
  def __init__(self, nameParam, items, start_time, end_time):
    self.name = nameParam
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "The " + self.name + " starts at " + str(self.start_time) + " and ends at " + str(self.end_time) + "."

  def calculate_bill(self, purchased_items):
    total = 0
    for food in purchased_items:
      quantity = purchased_items[food]
      price = self.items[food]
      total += price * quantity
    return total

#brunchmenu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

#early_bird
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

#dinner
dinner_items={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

#kids
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids menu', kids_items, 1100, 2100)

print(kids_menu)
print(brunch_menu)

brunch_order = {"pancakes": 1, "home fries" : 1, "coffee": 1}
print("cost of brunch order " + str(brunch_menu.calculate_bill(brunch_order)))

early_bird_order = {"salumeria plate": 1, "mushroom ravioli (vegan)" : 1}
print("cost of early bird order " + str(early_bird_menu.calculate_bill(early_bird_order)))

class Franchise:
   def __init__(self, address, menus):
     self.address = address
     self.menus = menus
   def __repr__(self):
     return self.address
   def available_menus(self, time):
     list_of_menus_available_at_that_time = []
     for menu in self.menus:
       if time > menu.start_time and time < menu.end_time:
         list_of_menus_available_at_that_time.append(menu)
     return list_of_menus_available_at_that_time

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))

class Business:
   def __init__(self, name, franchises):
     self.name = name
     self.franchises = franchises
franchises = [flagship_store, new_installment]
business_1 = Business("Basta Fazoolin' with my Heart", franchises)

arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Arepas', arepas_menu_items, 1000, 2000)
print(arepas_menu)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
business_2 = Business("Take a' Arepa", [arepas_place])
