
it_companies={"Facebook", "Google", "Microsoft", "Apple","IBM","Oracle", "Amazon"}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]


# #length of the set It_companies
print("the length of the set It_companies is",len(it_companies))

# #adding Twitter to it_companies list
it_companies.add("Twitter")
print(it_companies) 



# #inserting multiple companies into the set it_conmpanies
it_companies.update(["Cred", "Bharat pe",])
print(it_companies)



# #removing twitter from the set it_companies
print(it_companies)
it_companies.remove("Twitter")
print(it_companies)


# #difference between discard and remove
# #both remove and discard are used to remove elements from set but remove throws 'keyerror' when we try to remove an element which is not present
# #where as discard will not throw any error even if the element is not present in the set
# #when in doubt use discard as we are not sure if the element is not present in the set


# #join A and B using keyword called union
print("elements in A are",A)
print("elements in B are",B)
c = A.union(B)
print("after union",c)

# #intersecting A and B
print("elements in A are",A)
print ("elements in B are",B)
c = A.intersection(B)

# # Using the '&' operator
c = A & B
print("after intersecting",c)

# #Is A subset of B
# Using the issubset() method
result = A.issubset(B)
print (result)


# # #we can check are A and B disjoint sets with help of  isdisjoint method
result = A.isdisjoint(B)
print(result)

# # #joing a with b
c = A.union(B)
print(c)
#  and joining b with a

# c = A.union(B)
print(c)

# # #symmetric difference a and b
# # # Using the symmetric_difference() method
c = A.symmetric_difference(B)
print(c)

# #deleting the set completly with the keyword del
del it_companies
print(it_companies)


# #converting age list into a set
age_set=set(age)
print(age)


# #comparing the length of age_set and age_list
list_len=len(age)

age_set=set(age)
age_set_len=len(age_set)

print(list_len)
print(age_set_len)

if(list_len!=age_set_len):
    print("the length of set and list of the age are not same")













