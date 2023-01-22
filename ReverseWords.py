def reverse_words(text):
    reversedWords = []
    
    words = text.split(' ')
    
    for word in words:
        reversedWords.append(str(word[::-1]))
        
    return (' ').join(reversedWords)
    
  #go for it
