import time
questions = [
    ["Which of the following is a mutable data type in Python?","tuple", "string", "list", "int",3],
    ["What does len('hello') return?","4", "5", "6", "error",2],
    ["Which keyword is used to create a function in Python?","function", "def", "func", "define",2],
    ["Which of the following is NOT a Python data type?","list", "dictionary", "array", "tuple",3],
    ["What is the output of bool(0)?","True", "False", "0", "null",2]
    ]
prize_pool = [1,2,3,4,5]
sum_is = 0
k = 0

for i in questions:
    time.sleep(1)
    print(i[0])
    print(f"1.{i[1]}")
    print(f"2.{i[2]}")
    print(f"3.{i[3]}")
    print(f"4.{i[4]}")

    # we check the user ans
    ans = int(input("Enter your ans 1/2/3/4 : "))
    if ans == i[5]:
        print(f"congratulations buddy , correct ans ...now move towards the next questions")
         
    else:
        print(f"Wrong ans buddy , the correct ans was {i[5]} ")
        print("As you loose your reward is gone")
        print("Better luck next time !!!")
        break
    sum_is += prize_pool[k]
    k = k+1
    if k == 5:
        print(f"The total prize pool you won is {sum_is}")