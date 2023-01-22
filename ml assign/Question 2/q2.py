#creating an empty dictionary called dog
dog = dict()

#adding name, color, breed, legs, age to dog dictionary

dog.update({"name":"Fido", "color":"brown", "breed":"Golden Retriever", "legs":4, "age":3})
print(dog)

#creating a stident dictionary and adding first_name, last_name, gender, 
# age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student["first_name"] = "deeksha"
student["last_name"] = "ceeti"
student["gender"] = "Female"
student["age"] = 23 
student["marital_status"] = "Single"
student["skills"] = ["Python", "JavaScript", "Java"]
student["country"] = "United States"
student["city"] = "Kansas"
student["address"] = "13150 hadley street"

print (student)

#printing length of the student dictionary
print("the length of the student is",len(student))

#getting the values of the skills and datatypes
skills = student.get("skills")
print("the skills of the student are",skills)
print("the data type of the skills",type(skills))

# modifying the skills by adding skills
student["skills"].append("R")
print(student)

# dictionary keys as list
keys = list(student.keys())
print(keys)

# dictionary values as list
values = list(student.values())
print(values)