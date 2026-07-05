name = input("Enter Student Name: ")

m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))
m4 = int(input("Enter Marks of Subject 4: "))
m5 = int(input("Enter Marks of Subject 5: "))


total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
    print("Excelent")
elif percentage >= 75:
    print("Grade: B")
    print("Very Good")
elif percentage >= 60:
    print("Grade: C")
    print("Good")
elif percentage >= 40:
    print("Grade: D")
    print("Average")
else:
    print("Grade: Fail")
    print("VeryBad")