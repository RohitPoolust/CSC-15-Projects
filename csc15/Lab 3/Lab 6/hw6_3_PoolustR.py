# hw6_3_PoolustR.py
# Computes the student's grade and prints the ID with the grade
# Rohit Poolust
# 11.03.2021
# Lab 6

#from typing import Counter

# Computes scales that the user inputs
# Parameters: Nothing
# Return: The list that has the scale within


def getScale():

    scale_list= []


    scale1= int(input('Must be between 0 and 100:'))
    while scale1 <= 0 or scale1 > 97:
        scale1= int(input('Must be between 0 and 100:'))
    scale_list.append(scale1)



    #Scale 2 being compared to scale 1
    scale2=int(input('Must be between 0 and 100:'))
    while scale2 <= scale1 or scale2 >98:
        scale2=int(input('Must be between 0 and 100:'))
    scale1=scale2
    scale_list.append(scale1)

    #Scale 3 being compared to scale 2
    scale2= int(input('Must be between 0 and 100:'))
    while scale2 <= scale1 or scale2>99:
        scale2=int(input('Must be between 0 and 100:'))
    scale1=scale2
    scale_list.append(scale1)
  

    #Scale 4 being compared to scale 3
    scale2= int(input('Must be between 0 and 100:'))
    while scale2 <= scale1 or scale2 > 100:
        scale2=int(input('Must be between 0 and 100:'))
    scale1=scale2
    scale_list.append(scale1)



    return scale_list


#Computes the student ID and test scores of the students
#Parameters:None
#Returns the scores of each student
def getData():
    scores={}
    student_ID_scores= input('Enter students ID and test scores:')
    # 1 is equal to yes
    append=1
    #In order to stop the loop the user must enter the number 0 which is not in any interval for grades
    while student_ID_scores != '':
        if student_ID_scores[3] == ' ':
            list_scores=student_ID_scores.split()
        #Checks if student_ID is within range or else asks for new input
        id= int(list_scores[0])
        scores1= int(list_scores[1])

        if id < 100 or id > 999:
            append = 0

        #Checks if test_scores is within range or else asks for new input
        elif scores1 < 0 or scores1 > 100:
            append = 0
        
        if append == 1:
            scores[id]=scores1

        student_ID_scores= input('Enter students ID and test scores:')
        

    return scores
#Computes the grade of the student
#Parameters:scale which is a list and the individual score of a student
#Returns the individual grade for the student
def setGrade(scale,a_score):
    #If and Elif statments that figure out the scale in which the corresponding grade should be given
    if a_score <= scale[0]:
        return 'F'
    elif a_score <= scale[1]:
        return 'D'
    elif a_score <= scale[2]:
        return 'C'
    elif a_score <= scale[3]:
        return 'B'
    elif a_score > scale[3]:
        return 'A'

#Computes the scores and finds the average
#Parameters:scores
#Returns the average of the scores
def average(scores):
    #Takes counter and total variable and adds to them through the for loop ot obtain the average
    values_dic = scores.values()
    total=0
    counter=0
    for i in values_dic:
        total+=i
        counter+=1
    return total/counter

#Prints the scale 
#Parameters:scale that the user inputs
#Returns the scale
def printScale(scale):
    #Prints scale specific to the users scale
    for i in scale:
        if i == scale[0]:
            print(f'F {scale[0]} >= score')
        elif i == scale[1]:
            print(f'D {scale[0]} < score <= {scale[1]}')
        elif i == scale[2]:
            print(f'C {scale[1]} < score <= {scale[2]}')
        elif i == scale[3]:
            print(f'B {scale[2]} < score <= {scale[3]}') 
            print(f'A {scale[3]} < score')

#Prints the grades that were computed 
#Parameters:grades
#prints the student ID and score received by that student
def printGrades(grades):
    student_IDs=grades.keys()
    student_scoresLetter=grades.values()
    print("\n".join("{} {}".format(x, y) for x, y in zip(student_IDs, student_scoresLetter)))


#Actual main run
def main():
    #obtains the dictionary of ID and Scores
    dic_scores = getData()

    list_keys= dic_scores.keys()

    #obtains the boundaries of grades
    list_scale = getScale()

    grades={}

    #obtains the list of only values
    list_values = dic_scores.values()
    #this for loop finds the keys and list values and prints them inside the dictionary
    for j in list_keys:
        for i in list_values:
            student_grades = setGrade(list_scale,i)
            grades[j]=student_grades
    print(grades)
    
    print(average(dic_scores))
    printGrades(grades)


main()