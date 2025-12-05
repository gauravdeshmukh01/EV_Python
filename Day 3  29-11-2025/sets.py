nums={1,}
nums1={1,2,3,4}
nums2=set([1,2,3,4])
print(nums)
print(nums1)
print(nums2)

print(type(nums))
print(type(nums1))
print(type(nums2))

#no duplicate allowed
num={1,2,2,3}
print(num)

#True is a dup. of 1 and False is a dup. of 0
abc={1,True,2,False,3,4,0}
print(abc)

#check if a value is a set
print(2 in num)

#Add a new element to a set
print('')
num.add(8)
print(num)

#Add elements from one set to another
print('')
morenum={5,6,7}
num.update(morenum)
print(num)

#merge two sets to create a new set
one={1,2,3}
two={4,5,6}

mynewset=one.union(two)
print(mynewset)
