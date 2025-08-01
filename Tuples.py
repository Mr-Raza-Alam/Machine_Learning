'''
Tuples are the fundamental data structure ,used to store collections of items

its properties
i) immutable in nature means avoid modification/disallow any change in the exitsing tuples
ii) contains elements of diff. type 
iii) ordered and can contain duplicate elements

usage : use tuples to store collections of items which are needs to change like
 storing day's name in a week ,month's name  in a year,
 storing the record of sales of 2022 for the organisation
its syntax
 tupleName = ()
'''

empty_tuple = ()

#fruit tuple
fruits = ("Mango","Papaya","Banana")

# integers tuple
realNum = (4,2,12,6,-4,-7,2,4,-4)

#Mix items tuple
mix = ("Apple",5,12.5,True)


#Access tuple item -- it is same as list
print(fruits[0])
print(fruits[1])

#realNum[4] = -9 it doesn't support b/c tuples are immutable in nature

print(realNum[0:])

# methods in tuple are only count and index
# syntax .count(value) return no. of times the value is appeard in the tuple
print(realNum.count(2))
#syntax .index(value) return  idx of the given value/item
# actualSyntax  .index(value,si(optional,use to start search from si idx),ei(optional ,used to stop searching at ei idx))
print(fruits.index("Banana"))

print(type(mix))
