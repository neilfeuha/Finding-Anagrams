# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    #word = input('Enter word: ')
    #anagram = input('Enter word anagram: ')
    # convert word to lowercase
    word = word.lower()
    anagram = anagram.lower()

    # eliminate spaces between words
    word = word.split()
    anagram = anagram.split()

    # rejoin words to single word
    word = ''.join(word)
    anagram = ''.join(anagram)

    # convert word to word list
    word_list = list(word)
    anagram_list = []
    for letter in anagram:
        anagram_list.append(letter)

    # sort list
    sort_anagram = sorted(anagram_list)
    sort_words = sorted(word_list)
    print(sort_anagram)
    print(sort_words)

    # compare word list
    if sorted(word_list) == sorted(anagram_list):
        print("True")
    else:
        print("False")

    # return True


find_anagram("below", 'elbow')
