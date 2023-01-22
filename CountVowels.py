def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    letters = [*sentence]
    
    print(letters)
    
    count = 0
    
    for vowel in vowels:
        
        for letter in letters:
            
            if letter in vowel:
                count += 1
                
            
    print(count)
    return count
    
    pass

get_count('aeiou')
