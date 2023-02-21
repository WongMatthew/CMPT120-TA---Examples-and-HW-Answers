def pynum(h):
    for i in range(1, h+1):
        for j in range(h-i):
            print(" ", end = "")
        for k in range(1,i+1):
            print(k, end= " ")
        for l in range(i-1, 0, -1):
            print(l, end = " ")
        print()

def function():
    h = int(input("What is the height of the pyramid?\n"))
    if h not in range(2,10):
        print("PyNum cannot help you!")
    else:
        pynum(h)
        
function()