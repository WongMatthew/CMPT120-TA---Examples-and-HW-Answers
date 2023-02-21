def SubstringFinder2(source, target):
    source_len = len(source)
    target_len = len(target)
    
    for i in range(source_len - target_len + 1):
        j = 0
        while j < target_len:
            if source[i + j] != target[j]:
                break
            j += 1
        
        if j == target_len:
            return i
    
    return -1