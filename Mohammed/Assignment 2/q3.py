def PaNNaP(source):
    source_list = []
    source_len = len(source)
    
    for i in range(source_len):
        if source[i] >= 'a' and source[i] <= 'z':
            source_list.append(source[i])
        elif source[i] >= 'A' and source[i] <= 'Z':
            source_list.append(chr(ord(source[i]) + 32))
    
    source_list_len = len(source_list)
    for i in range(source_list_len//2):
        if source_list[i] != source_list[source_list_len-i-1]:
            print("No")
            return
    
    print("Yes")