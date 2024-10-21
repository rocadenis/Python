import math 

# ex_1: generare secventa fibonacci
def ex_1(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    
    return fib_list

# ex_2: gasire numere prime
def ex_2(listOfNumbers):
    listOfPrimeNumbers = []
 
    for number in listOfNumbers:
        isPrime = True
        if number < 2 or (number % 2 == 0 and number != 2):
            isPrime = False
        for divider in range(3, int(math.sqrt(number) + 1), 2):
            if number % divider == 0:
                isPrime = False
                break
        if isPrime:
            listOfPrimeNumbers.append(number)
 
    return listOfPrimeNumbers

# ex_3: operatii pe seturi
def ex_3(a, b):
    a_set = set(a)
    b_set = set(b)
    
    intersection = list(a_set & b_set)
    union = list(a_set | b_set)
    a_minus_b = list(a_set - b_set)
    b_minus_a = list(b_set - a_set)
    
    return (intersection, union, a_minus_b, b_minus_a)

# ex_4: compunere melodie
def ex_4(a, b, startingNotePosition):
    song = [a[startingNotePosition]]
    position = startingNotePosition

    for i in range(len(b)):
        position += b[i]
        if position >= len(a) or position < 0:
            position = position % len(a)
        song.append(a[position])

    return song

# ex_5: eliminare elemente sub diagonala
def ex_5(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, rows):
        for j in range(0, cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

# ex_6: elemente repetate
def ex_6(x, *lists):
    all_lists = []
    result = []
    
    for i in lists:
        all_lists += i
    
    for lst in all_lists:
        if all_lists.count(lst) == x and lst not in result:
            result.append(lst)
    
    return result  

# ex_7: palindromi
def ex_7(listOfNumbers):
    listOfPalindroms = []
    biggestPalindrom = 0
    
    for number in listOfNumbers:
        if str(number) == str(number)[::-1]:
            listOfPalindroms.append(number)
            if biggestPalindrom < number:
                biggestPalindrom = number

    return len(listOfPalindroms), biggestPalindrom 

# ex_8: filtrare caractere
def ex_8(x=1, listOfWords=None, flag=True):
    if listOfWords is None:
        listOfWords = [] 

    result = []
    
    for word in listOfWords:
        listOfCharacters = []
        for character in word:
            if flag:
                if ord(character) % x == 0:
                    listOfCharacters.append(character)
            else:
                if ord(character) % x != 0:
                    listOfCharacters.append(character)
        result.append(listOfCharacters)
    
    return result

# ex_9: spectatori
def ex_9(matrix):
    listOfPositions = []

    for row in range(1, len(matrix)):  
        for col in range(len(matrix[row])):  
            current_value = matrix[row][col]
            
            for prev_row in range(row):
                if current_value <= matrix[prev_row][col]:
                    listOfPositions.append((row, col))
                    break  

    return listOfPositions

# ex_10: lista de tuple in functie de pozitite
def ex_10(*lists):
    maxNrOfElements = max(len(lst) for lst in lists) #cea mai lunga lista 
    listOfTuples = []
    
    for i in range(maxNrOfElements):
        currentTuple = () #stochez elem intr un tuplu nou 
        for lst in lists:
            try:
                currentTuple += (lst[i],)  
            except IndexError: 
                currentTuple += (None,) 
        listOfTuples.append(currentTuple)

    return listOfTuples

# ex_11: sortare dupa caracter
def ex_11(lists):
    n = len(lists)

    for i in range(n):
        for j in range(0, n - i - 1): #n-i-1 sa nu compar un tuplu cu el insusi 
            if len(lists[j][1]) > 2 and len(lists[j + 1][1]) > 2: #verific sa am minim 3 caractere in ambele 
                chr1 = lists[j][1][2]  
                chr2 = lists[j + 1][1][2]
                if ord(chr1) > ord(chr2):
                    lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists

# ex_12: grupare rimata
def ex_12(words):
    rhyme_dict = {}

    for word in words:
        rhyme_key = word[-2:]  # ia ultimele doua caractere
        if rhyme_key in rhyme_dict:
            rhyme_dict[rhyme_key].append(word)
        else: # daca cheia nu exista fac o intrare noua in disctionar 
            rhyme_dict[rhyme_key] = [word]

    grouped_rhymes = list(rhyme_dict.values())

    return grouped_rhymes

if __name__ == '__main__':
    #ex 1
    print("ex1:\n", ex_1(8), "\n")

    #ex 2
    print("ex2:\n", ex_2([1, 2, 3, 4, 5, 7, 9, 11, 12, 25]), "\n")

    #ex 3 
    print("ex3:\n", ex_3([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]),"\n")

    #ex 4
    print("ex4:\n", ex_4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2), "\n")

    #ex 5
    result = ex_5([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
    print("ex5:\n", result, "\n")

    #ex 6
    print("ex6:\n", ex_6(3, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]), "\n")

    #ex 7
    print("ex7:\n", ex_7([12321, 1234321, 57875, 146]), "\n")

    #ex 8
    print("ex8:\n", ex_8(2, ["test", "hello", "lab002"], False), "\n")

    #ex 9 
    print("ex9:\n", ex_9([[1, 2, 3, 2, 1, 1],
                       [2, 4, 4, 3, 7, 2],
                       [5, 5, 2, 5, 6, 4],
                       [6, 6, 7, 6, 7, 5]]), "\n")
    
    #ex 10
    print("ex10:\n", ex_10([1, 2], [5, 6, 7], ["a", "b", "c"]), "\n")

    #ex 11
    print("ex11:\n", ex_11([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'yyc')]), "\n")

    #ex 12
    print("ex12:\n", ex_12(['ana', 'banana', 'carte', 'arme', 'parte']), "\n")
