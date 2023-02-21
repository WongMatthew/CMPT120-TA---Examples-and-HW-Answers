text = input('Hi, this is Pchatbot, can I talk to you?\n')
if text in {'Y', 'y'}:
    name = input('What is your name?\n')
    print(f'Nice to meet you, {name}.')
    feeling = input('How are you doing today?\n').lower()
    if feeling in {'good', "i'm great", "i'm good",'fine'}:
        print(f"I'm glad you're feeling well, {name}.")
        print("I'm glad you're feeling well,"+name+".")
    elif feeling in {'bad', 'not okay'}:
        print('Have some time to yourself to recharge!')
    else: 
        print('I see!')
    try:
        age = int(input("How old are you?\n"))
        if age > 18 and feeling in {'good', "i'm great", "i'm good",'fine'}:
            print("You are ready to drive.")
        else:
            print('Still taking the bus!')
    except ValueError:
        print('Invalid age input!')
elif text in {'N','n'}:
    print('Okay! Talk to you soon!')