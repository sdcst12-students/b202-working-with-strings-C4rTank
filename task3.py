#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''

def split(input):

    #parameters
    #str input - string to be split

    input = list(input)
    count = len(input)
    count = count / 2
    count = count + 0.5
    count = int(count)

    input.insert(count, "\n")
    input = "".join(input)

    print(input)

    #return
    #str new string with line break in the middle

    modifiedString = input
    return modifiedString


if __name__ == "__main__":
    sentence = "There is a big ball-oon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a \nfat cat"

#DONE