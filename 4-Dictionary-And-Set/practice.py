marks = {}

x = int(input("Enter number of physics marks : "))
marks.update({"physics": x})

x = int(input("Enter number of chemistry marks : "))
marks.update({"chemistry": x})

x = int(input("Enter number of mathematics marks : "))
marks.update({"mathematics": x})

print(marks)