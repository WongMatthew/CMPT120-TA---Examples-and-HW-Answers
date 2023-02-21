def find_substring(source, k):
    max_substring = ""
    max_unique_characters = 0
    for i in range(len(source) - k + 1):
        substring = source[i:i+k]
        unique_characters = len(set(substring))
        if unique_characters > max_unique_characters:
            max_substring = substring
            max_unique_characters = unique_characters
    return max_substring

while True:
    source = input()
    if source == "quit":
        break
    k = int(input())
    print(find_substring(source, k))