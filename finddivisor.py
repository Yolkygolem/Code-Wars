def divisors(integer):
    
    divisors = [*range(2, integer + 1, 1)]
    intsDivisors = []
    
    for divisor in divisors:
        if integer % divisor == 0:
            intsDivisors.append(divisor)
        
    if len(intsDivisors)== 1 and intsDivisors[0] == integer:
        print(intsDivisors)
        return str(integer) + ' is prime'
                
    elif intsDivisors[-1] == integer:
        intsDivisors.remove(integer)
        
    print(intsDivisors)
    pass

divisors(56)
