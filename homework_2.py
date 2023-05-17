eleks_employees = ["Nataly", "John", "Peter", "James", "Jacob"]
toshiba_employees = ["Nelly", "Harry", "Jimmy", "Natan", "Mark"]
toshiba_employees.extend(eleks_employees)
eleks_employees.clear()
print(f"Toshiba employees: {toshiba_employees}")
print(f"Elex employees: {eleks_employees}")

casino_blacklist = {"Nataly Parker", "John Smith", "Peter Prent", "James Jacob", "Jacob Hammer"}
poker_blacklist = {"Nataly Parker", "Smith Janny", " Prent Harem", "James John", "Hammer Henthon"}
alcohol_blacklist = {"Nataly Parker", "Perry Janny", " Oleh Harem", "Jerens John", "Hammy Henthon"}
total_blacklist = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(total_blacklist)

vegeterians_list = ["Natali"]
omnivores_list = ["Alex"]
omnivores_list.extend(vegeterians_list)
print(omnivores_list)

vegeterians_list = ["Natali"]
omnivores_list = ["Alex"]
eating_greens = []
eating_greens.extend(omnivores_list + vegeterians_list)
print(f"People who can eat everything: {eating_greens}")

vip_box = ("Hanna", "Helen", "Joye")
common_room = ["Peter", "Jeniffer"]
common_room.append([])
print(vip_box)
print(common_room)

group_of_people = ["John Dow", "Marta Dow", "John Dow"]
group_of_people.remove("John Dow")
print(group_of_people)
