import W3D as cs
import pandas as pd
import numpy as np

def Sequential(work,data1,alpha, beta, columnDecision, dec,a):
    columns = a
    tmp = []
    tmp.append(columnDecision)
    for x in range(len(columns)):
        tmp.append(columns[x])
        tmpMatrix = data1[tmp]
        print("columns considered: ", tmp)
        print("INDISCERNIBILITY CLASSES: ", "\n", len(work.Indiscernibility(tmpMatrix)))
        print("POSITIVE REGION :", "\n",float((int(len( work.Positive(tmpMatrix, alpha, columnDecision, dec)))*100)/int(len(data1))),'%')
        print("NEGATIVE REGION :", "\n",float((int(len( work.Negative(tmpMatrix, beta, columnDecision, dec)))*100)/int(len(data1))),'%')
        print("BOUNDARY REGION :", "\n",float((int(len( work.Boundary(tmpMatrix, alpha, beta, columnDecision, dec)))*100/int(len(data1)))),'%')
        print("ROUGHNESS: ", "\n", work.Roughness(tmpMatrix,alpha,beta,columnDecision,dec), " %")

data = pd.read_csv('car.csv', sep=',',header = None)
a=pd.read_csv('sequential.csv', sep=',')
a=list(a.columns)

data.columns = ['Price', 'Maintenance', 'Number of Doors', 'Capacity', 'Size of Luggage Boot', 'Safety', 'Decision']
work = cs.TWDPackage(data)

try:
    alpha = float(input("Please provide alpha(between 0 and 1): \n"))
    beta = float(input("Please provide beta(between 0 and 1): \n"))
except ValueError:
    print("Error in the input, try again: \n")
    alpha=float(input("Please provide a number as alpha(between 0 and 1): \n"))
    beta = float(input("Please provide a number ad beta(between 0 and 1): \n"))

valuedecision= list(data['Decision'].unique())
valueinput= input("Please provide the attribute decision (unacc, acc , good, vgood) \n")
if valueinput in valuedecision:
    Sequential(work,data,alpha, beta, 'Decision', valueinput,a)
else:
    print('\n' "Try again,value not present \n")


