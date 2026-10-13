#Start with a dictonary of student names and marks, then calculate 
# average, highest, and lowest marks. Then list who passed and who failed
# and finally print a neat report.

#Algorithm:

#1.Creating the dictonary
#2.Taking input
#3.Calculating avg, high and low marks
#4.Printing passed student report
#5.Printing failed student report

#1.

students ={
		"Ram":78,
		"Hari":88,
		"Shyam":98,
		"Geeta":68,
		"Sita":58,
		"Prakash":23,
		"Pita":89,
		"Dogesh":34,
		"Kira":11,
		"Hage":8
}
#print(len(students));
#print(students);
#print(students["Sita"]);
#print(students["Shyam"]);
#print(f"Total students: {len(students)}");
#for name in students:
# 	#print(f"{name} scored: {students[name]}")
total = 0;
for value in students.values():
	total += value;
# print(f"Total: {total}");

#average:
average = total/len(students)
print(f"Average Marks: {average}")

#checking pass or fail
pas = 0
fail = 0
for name in students:
	if students[name]<40:
		print(f"{name} : {students[name]} - Failed")
		fail+=1
	else:
		print(f"{name} : {students[name]} - Passed")
		pas+=1

print(f"No of students passed:{pas}, failed:{fail}")

max_value = list(students.values())[0]
top_student = list(students.keys())[0]
# for value in students.values():
# 	if value > max_value:
# 		max_value = value
# for key,value in students.items():
# 	if value == max_value:
# 		print(f"Top student is {key} : {max_value}")
print(top_student)

for key,value in students.items():
	if value > max_value:
		max_value = value
		top_student = key
print(f"Top Student is {top_student}: {max_value}")