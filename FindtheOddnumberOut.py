def find_it(seq):
    
    numbers = seq
    arrayLength = len(numbers)
    
    for number in range(0, arrayLength):
        count = 0
        for num in range(0, arrayLength): 
            if numbers[number] == numbers[num]:
                count += 1
        if (count % 2 != 0):
            return(numbers[number])
    
    return None
