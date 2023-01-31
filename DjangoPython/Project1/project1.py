
print("      Project 1: Python basics ")
print("--------- Exams and Scores ---------------")
print("")
scores = input("Give a set of scores(separeted by comma), please: ")
aux = scores.split(",")

weight = input("Give a set of weight(separeted by comma), please: ")
aux2 = weight.split(",")

while(len(aux)!=len(aux2)):
    print("The amount of scores and weights must be the same. Please give the same amount of weights as scores!")
    weight = input("Give a set of weight(separeted by comma), please: ")
    aux2 = weight.split(",")
    
a = list(map(float,aux))
b = list(map(float,aux2))   
sum = 0
sumWeight = 0
for i in range(len(aux)):
    d = (a[i]*b[i])
    sum = d+sum
    sumWeight = sumWeight + b[i]
resultt = (sum/sumWeight)
print("")
print("The result of the weighted average of the scores is: ", resultt)



    
