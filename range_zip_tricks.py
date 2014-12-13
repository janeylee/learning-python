####Example 1
months = ['January','February','March','April','May','June','July','August','September','November','December']
 
month_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
def find_the_month(l1,l2):
    month_dict = {}
    length = len(l1)
    for i in range(0,length):     #RANGE 
        month_dict[l1[i]] = l2[i]
    return month_dict
 
 
####Example 2
 
def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for n in number_list:
        total = total + n
    return total
 
def report_card():
    report_card = []
    allnames = []
    grades = []
    num_classes = input("How many did classes did you take? ")
        
    for value in range(num_classes):
        name = raw_input("What was the name of this class? ")
        grade = input("What was your grade? ")
        allnames.append(name)
        grades.append(grade)
 
    print "allnames", allnames
    print "grades", grades
    print "range(num_classes)", range(num_classes)
 
    print "REPORT CARD"
 
    for name, grade in zip(allnames, grades)    ##SEE ZIP TRICK HERE. Loops over two lists at once
        print name, "-", grade
 
    gpa = float(sum_all(grades)/len(grades))
    print "Overall gpa: ", gpa
    return report_card
 
report_card()
