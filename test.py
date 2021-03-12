from solution import challenge

def test(pathInput, pathOutput):
    '''
    Description
        Test challenge.
        Requires the function challenge(words, matrix)
        to return the result in the same order of the words
        input argument
    Arguments
        pathInput: string
        pathOutput: string
    Returns
        result: bool
    '''
    # code

    # 1 - read input dataset
    with open(pathInput, 'r') as g:
        f = g.readlines()

    # 2 - prepare input dataset
    nWords, nRows, nCols = [int(s) for s in f[0].split()]

    words = []
    for i in range(nWords):
        words.append(f[i + 1].strip('\n'))

    matrix = []
    aux = nWords + 1
    for i in range(nRows):
        matrix.append(list(f[i + aux].strip('\n')))

    # 3 - call hunting-words.py
    result = challenge(words, matrix)
    # result = {'google': 4, 'morosidade':1, 'coragem':2}

    # 4 - compare outputs
    with open(pathOutput, 'r') as g:
        f = g.readlines()

    control = []
    for i in f:
        control.append(int(i))

    validation = 0
    for i in range(nWords):
        validation += (control[i] == result[words[i]])

    return validation == nWords

if __name__ == '__main__':
    import sys
    path_input = sys.argv[1]    # exemple  <- data/input_N.txt
    path_output = sys.argv[2]   # exemple  <- data/output_N.txt
    test(path_input, path_output)