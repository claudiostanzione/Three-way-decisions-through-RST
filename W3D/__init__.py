import pandas as pd
import numpy as np
class TWDPackage:
    def __init__(self, matrix):
        self.matrix = pd.DataFrame(matrix)
    
    def Indiscernibility(self, matrixApp):

        emptgroup=[]
        group=[]
        tmp = matrixApp
        columns = list(tmp.columns)
        columns.pop(0)
        data1= tmp[columns]
        replicate=data1[data1.duplicated(keep=False)]
        replicaone=replicate.groupby(replicate.columns.tolist()).apply(lambda x: x.index.tolist()).values.tolist()
        replicatwo=data1.duplicated(keep=False)
        wher=np.where(replicatwo==False)
        for w in wher:
            alone=data1.index[w]
        for y in alone:
            emptgroup.append(y)
            group.append(emptgroup)
            emptgroup=[]
        for z in replicaone:
            group.append(z)
        return group
    def Concept(self,var1, var2):
        return self.matrix[(self.matrix[var1]==var2)].index
    def Positive(self,matrixApp, alpha, var1, var2):
        lower1=[]
        lower=[]
        first = self.Indiscernibility(matrixApp)
        second = self.Concept(var1, var2)
        for items in first:
            cont=0
            for item in items:
                if item in second:
                    cont+=1 
            prob=cont/len(items)
            if prob>=float(alpha):
                lower1.append(items)
        for k in lower1:
            for l in k:
                lower.append(l)
        return lower
    def Negative(self,matrixApp, beta, var1, var2):
        upper1=[]
        upper=[]
        first = self.Indiscernibility(matrixApp)
        second = self.Concept(var1, var2)
        for items in first:
            cont=0
            for item in items:
                if item in second:
                    cont+=1 
            prob=cont/len(items)
            if prob<=float(beta):
                upper1.append(items) 
        for k in upper1:
            for l in k:
                upper.append(l)
        return upper
    def Boundary(self,matrixApp, alpha, beta, var1, var2):
        bound1=[]
        bound=[]
        first = self.Indiscernibility(matrixApp)
        second = self.Concept(var1, var2)
        for items in first:
            cont=0
            for item in items:
                if item in second:
                    cont+=1 
            prob=cont/len(items)
            if (prob<float(alpha) and prob > float(beta)) :
                bound1.append(items) 
        for k in bound1:
            for l in k:
                bound.append(l)
        return bound
    def Roughness(self,matrixApp,alphac,beta, var1,var2):
        lower1=[]
        lower=[]
        upper1=[]
        upper=[]
        first = self.Indiscernibility(matrixApp)
        second = self.Concept(var1, var2)
        for items in first:
            cont=0
            for item in items:
                if item in second:
                    cont+=1 
            prob=float(cont/len(items))
            if prob>=float(alphac):
                lower1.append(items)
            if prob > float(beta):
                upper1.append(items)
        for k in lower1:
            for l in k:
                lower.append(l)
        for j in upper1:
            for i in j:
                upper.append(i)
        try:
            return float((len(lower)/len(upper))*100)
            
        except ZeroDivisionError:
            return 0
                    
                
                
            
                
    
    