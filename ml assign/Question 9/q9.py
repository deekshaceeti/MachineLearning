#program which reads weights of N 
# students into a list and convert weights to kilos in seperate list using loop

lbs = []
kgs = []
N = int(input("Enter the number of students: "))

for i in range(N):
    weight = float(input("Enter the weight of student {} in pounds: ".format(i+1)))
    lbs.append(weight)

for weight in lbs:
    kg = weight * 0.453592
    kgs.append(kg)

print("Weights in pounds: ", lbs)
print("Weights in kilograms: ", kgs)
