def narcissistic( value ):
    
    numbers = []
    
    for number in str(value):
        numbers.append(int(number))
    
    sumOfNum = []  
    for number in numbers:
        
        
        lenOfNum = len(str(value))
        sumOfNum.append(number ** lenOfNum)
        
    if sum(sumOfNum) == value:
        print(str(value) + ' is narcissistic')
        return True
        
    else:
        print(str(value) + ' is not narcissistic')
        return False
        
print(narcissistic(12))
