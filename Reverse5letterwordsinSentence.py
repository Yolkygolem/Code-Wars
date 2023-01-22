def spin_words(sentence):
    words = sentence.split()
    
    count = 0
    
    for word in words:
        length = [*word]
        
        if len(length) >= 5:
            length.reverse()
            reversedword = ''.join(length)
            words[count] = reversedword
        
        
        count += 1
        
    return(' '.join(words))
    pass
