class AreaRect:             #Declaration of Class
    def __init__(self,l,b):  #Constructor
        self.l=l
        self.b=b
    def calculateArea(self):   # declaration Of method
        return self.l * self.b

area1=AreaRect(5,6)     #Object Creation
area2=AreaRect(10,20)
print(area1.calculateArea())  #Calling Method
