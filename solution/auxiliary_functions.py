import string
import random

def validation(words, matrix):
    '''
    Description
        Validation
    Arguments
        words: list
        matrix: matriz
    Return
        result: tuple (status: bool, msg: string)
    '''
    return True, ""

def randomMatrixGeneration(n,words):
    """
    Description
        Random square matrix of string generator 
        Fit the words randomly in matrix
        Library used: random and string

    Arguments    
        n - dimension of square matrix
        words = ['word1','word2','word3',...,'wordn']

    Returns
        matrix[n][n] - list of lists

    Observations:
        I didn't think of a way for words to respect the 
        place of others, so depending on the random position, 
        the words can overlap.    
    """    
    chars = string.ascii_uppercase + string.ascii_lowercase
    
    matrix = []

    for i in range(n):
        matrix.append([' '] * n)
    
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.choices(chars)[0]

    for k in range(len(words)):
        indl = random.randint(0,n-1)
        indc = random.randint(0,n-1)    

        if indl + len(words[k]) <= n: 
            if indc + len(words[k]) <= n:
                for i in range(len(words[k])):
                    matrix[indl+i][indc+i] = words[k][i]        

            elif indc + len(words[k]) > n:
                if indc - len(words[k]) >= 0:
                    if indl - len(words[k]) >= 0:
                        for i in range(len(words[k])):
                            matrix[indl-i][indc-i] = words[k][i]        
        else:
            if indc - len(words[k]) >= 0:
                for i in range(len(words[k])):
                    matrix[indl-i][indc-i] = words[k][i]        

    return matrix

def solver(matrix,words):
    """
    Description
        Function to find words
        No library used 

    Inputs
        Quadratic matrix - square list of lists
        example:
            [['Q','r','x','y','W', ... ,'P','u'],     
             ['Q','r','x','y','W', ... ,'P','u'],
             ['Q','r','x','y','W', ... ,'P','u'],
               
               .       .       .   .         .
               .       .       .      .      . 
               .       .       .         .   .

             ['Q','r','x','y','W', ... ,'P','u']]

        words = ['word1', 'word2', 'word3']

    Returns
        - Position of word about diagonal relation
        - Directions of word - top to bottom or bottom to top
        - FoundWords, that means the words in the matrix
    """
    
    positions = []
    directions = []
    foundWords = []

    minLenght = 10000
    for word in words:
        if len(word) < minLenght:
            minLenght = len(word)
 
    n = len(matrix[0])
    diag = 2*(n - minLenght) 

    for k in range(diag):
        if k < diag/2: # Abaixo da diagonal principal = 3    
            letters = ''
            for i in range(n - int(diag/2 - k)):
                letters += matrix[int(diag/2 - k + i)][int(i)]

            for word in words:
                if len(word) <= len(letters):
                    if word in letters:
                        directions.append("Top-Bottom")
                        positions.append(3)
                        foundWords.append(word)

                    elif word[::-1] in letters:
                        directions.append("Bottom-Top")            
                        positions.append(3)
                        foundWords.append(word)

        if k == diag/2: # na diagonal principal = 1
            letters = ''
            for i in range(n):
                letters += matrix[int(i)][int(i)]

            for word in words:
                if len(word) <= len(letters):
                    if word in letters:
                        directions.append("Top-Bottom")
                        positions.append(1)
                        foundWords.append(word)

                    elif word[::-1] in letters:
                        directions.append("Bottom-Top")
                        positions.append(1)
                        foundWords.append(word)

        if k > diag/2: # acima da diagonal principal = 2
            letters = ''
            for i in range(n - int(k - diag/2)):
                letters += matrix[int(i)][int(k - diag/2 + i)]

            for word in words:
                if len(word) <= len(letters):
                    if word in letters:
                        directions.append("Top-Bottom")
                        positions.append(2)
                        foundWords.append(word)

                    elif word[::-1] in letters:
                        directions.append("Bottom-Top")            
                        positions.append(2)
                        foundWords.append(word)

    return positions, directions, foundWords
