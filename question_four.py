#(i)
list_one=[1]
print(list_one)
list_one.append(12)
print(list_one)
list_one.append(123)
print(list_one)
list_one.append(1234)
print(list_one)
list_one.append(12345)
print(list_one)


#(ii)
def factorialOfNumber(n):
    factorial= n*1*2*3*4*n
    print("The factorial is ",factorial)
factorialOfNumber(5)  

#(iii)
def sumOfNumbers(a,b):
    sum=a+b
    print("The sum is",sum)
sumOfNumbers(3,4) 


#(iv)   
class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
        
 #(v)       
Car_one=Car("Toyota",2018)   
print(Car_one.brand ,Car_one.year) 
    
        
        