list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []
even_numbers = []
for index in range(len(list_of_elements)):
    if index % 2 == 0:
        even_numbers.append((index, list_of_elements[index]))
    else:
        odd_numbers.append((index, list_of_elements[index]))
print(tuple(odd_numbers))
print(tuple(even_numbers))

variable = 2
print(variable * 2)
print(variable.conjugate() * 2)
print(int(variable / 2))
print(int(variable // 2))

lists_of_names_friends = ["John", "Marta", "James"]
lists_of_enemies = ["John", "Johnatan", "Artur"]
for names in lists_of_names_friends:
    if names in lists_of_enemies and names != "James":
        print(f"We are not friends anymore: {names}")

