# Name:Janey
# Section: None!
# hw3.py
 
# **********  Exercise 3.1 ********** 
 
def list_intersection(first_list, second_list):
    newlist = []
    for item in first_list:
        if item in second_list:
            newlist.append(item)
    return newlist
 
print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])
 
# **********  Exercise 3.2 **********
 
# Define your function here
def ball_collide((x, y, r), (a, b, z)):
    distance_betw_centers = ((x-a)**2 + (y-b)**2)**0.5
    sum_of_radii = r + z
    if distance_betw_centers <= sum_of_radii:
        return True
    return False
 
 
# Test Cases for Exercise 3.2
print "test1", ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print "test2", ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print "test3", ball_collide((7, 8, 2), (4, 4, 3)) # Should be True
 
 
# **********  Exercise 3.4 **********
 
NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
 
# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    length = len(l1)
    for i in range(0,length):
        comb_dict[l1[i]] = l2[i]
    return comb_dict
 
print combine_lists(NAMES, AGES)
 
combined_dict = combine_lists(NAMES, AGES)
 
def people(age):
    da_list = []
    if 18 <= age and age <= 22:
        for key, value in combined_dict.items(): # loops over both key and value
            if combined_dict[key] == age:
                da_list.append(key)        
    return da_list
    
 
 
# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []
 
 
 
# **********  Exercise 3.5 **********
 
months = ['January','February','March','April','May','June','July','August','September','November','December']
 
month_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
def find_the_month(l1,l2):
    month_dict = {}
    length = len(l1)
    for i in range(0,length):
        month_dict[l1[i]] = l2[i]
    return month_dict
 
month_dictionary =  find_the_month(months, month_nums)
 
def zellers(month, date, year):
 
    month = month_dictionary[month]
    firsttwo = int(str(year)[-2])
    lasttwo = int(str(year)[0:1])
    
    if month >= 3:
        month = month - 2
    elif month < 3:
        month = month + 10
        lasttwo = lasttwo - 1
    
    w = (13*month - 1)/5
    x = lasttwo/4
    y = firsttwo/4
    z = w + x + y + lasttwo + date - 2*firsttwo
    r = z % 7
 
    if r == 0:
        return "Sunday"
    elif r == 1:
        return "Monday"
    elif r == 2:
        return "Tuesday"
    elif r == 3:
        return "Wednesday"
    elif r == 4:
        return "Thursday"
    elif r == 5:
        return "Friday"
    elif r == 6:
        return "Saturday"
 
print zellers("March", 10, 1940)
