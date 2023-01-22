age=[19,22,19,24,20,25,26,24,25,24]
#sorting the list and finding the min and max
age.sort()
print(age)
#finding min and max
print(min(age))
print(max(age))
#finding the median in the list age

age.sort()
length = len(age)

if length % 2 == 0:
    median = (age[length//2-1] + age[length//2]) / 2
else:
    median = age[length//2]

print(median)



#average in list using sum of all divided by numbers

average = sum(age) / len(age)
print("the average of the list is",average)

#range of this list

range = max(age) - min(age)
print("the range of the list is",range)
