#grading program Jonathan De la Cruz 

print "Hello! Welcome to Jonny's Grading Book!"
print " ....Please don't enter decimals "

m_grade = input("Enter your grade for Math: ")
sc_grade = input("Enter your grade for Science: ")
ss_grade = input("Enter your grade for Socal Studies: ")
en_grade = input("Enter you grade for English: ")
ec_grade = input("Enter grade for Extra Curricular: ")

grade_list = [int(m_grade),int(sc_grade),int(ss_grade),int(en_grade),int(ec_grade)]
print "Grade list: "
print grade_list

listSum = sum(grade_list)
listLength = len(grade_list)
listAverage = listSum / listLength
grade_list.append(listAverage)
print "Your average grade: "
print "listAverage " + str(listAverage) 


if listAverage < 60:
    print "Get does grades up! you have a U "
        
if listAverage >= 60 and listAverage < 70:
    print "Get does grades up! you have a D "
        
if listAverage >= 70 and listAverage < 80:
    print "Theres work to do! you have a C "
        
if listAverage >= 80 and listAverage < 90:
    print "Your almost there! you have a B "
        
if listAverage >= 90:
    print "you made it! you have an A!" 
    

print "Thank you for using Jonny's Grading Book"
