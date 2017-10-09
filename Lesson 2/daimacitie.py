import random
secret = random.randint(1,10)
#secret = 8
print("猜数字")
temp = input("please:")
while temp.isdigit() == 0:
    temp = input("请输数字:")
guess = int(temp)
round = 1
while guess != secret and round <10:
    round = round + 1
#    temp = input("again:")
#    guess = int(temp)
    if guess > secret:
        print("big")
        temp = input("again:")
        while temp.isdigit() == False:
            temp = input("请输数字:")
        guess = int(temp)
    else:
        if guess <secret:
            print("small")
            temp = input("again:")
            while temp.isdigit() == False:
                temp = input("请输数字:")
            guess = int(temp)
        else:
            print("good")
if round == 1:
    print("恭喜你，答对了，bye")
else:
    print("bye")
