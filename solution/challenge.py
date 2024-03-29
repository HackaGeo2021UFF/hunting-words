from solution.auxiliary_functions import *


def challenge(words, matrix):
    '''
    Description
        Hunting words.
            * 1 word "X" in main diagonal
            * 2 word "X" above the main diagonal
            * 3 word "X" bellow the main diagonal
            * 4 word "X" doesn't exist
    Arguments
        words: list
        matrix: list of lists NxN
    Return
        result: dic {Key: word (str), Value: resposta (int)}
    '''


    positions, _, foundWords = solver(matrix, words)

    x = list(set(words).difference(foundWords))

    dic = {foundWords[i]: positions[i] for i in range(len(positions))}

    if len(x) > 0:
        for j in x:
            dic.update({j : 4})

    return dic
