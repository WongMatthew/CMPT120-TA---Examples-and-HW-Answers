def AnagramSolver(list):
    # This function will ask for a list of words and check which words in the list are anagrams of each other
    # Output: maximum number of anagrams in the list
    # Input: list of words 
    max_counter = 1
    for i in range(len(list)):
        counter = 1
        for j in range(i+1,len(list)):
            if sorted(list[i]) == sorted(list[j]):
                counter += 1
        if counter > max_counter:
            max_counter = counter
    print(max_counter)

def main():
    num = input("Enter the number of words: ")
    wordlist = []
    for i in range(int(num)):
        word = input("Enter the word: ")
        strip_word = word.replace(" ","").replace(",","").lower()
        wordlist.append(strip_word)
    AnagramSolver(wordlist)

main()