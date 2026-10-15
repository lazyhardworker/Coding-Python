students ={
		"Ram":78,
		"Hari":88,
		"Shyam":98,
		"Geeta":68,
		"Sita":98,
		"Prakash":23,
		"Pita":89,
		"Dogesh":34,
		"Kira":11,
		"Hage":8
}
#printing only the first student with 98
for name,value in students.items():
	if value == 98:
		print(f"{name} got score: {value}")
		break
#printing only the last student with 98
print("________________________________________")

for name,value in reversed(students.items()):
	if value == 98:
		print(f"{name} got score: {value}")
		break

#printing both students getting 98
print("________________________________________")
for name,value in students.items():
	if value == 98:
		print(f"{name} got score: {value}")

#printing only the last student with 98 without using reversed
print("________________________________________")

max_value = list(students.values())[0]

for value in students.values():
	if value > max_value:
		max_value = value

last_name = ""

for key,value  in students.items():
	if value == max_value:
		last_name = key
print(f"{last_name} got score: {max_value}")