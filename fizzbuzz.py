def fizzBuzz():
    while True:
        print('Input an Interger')
        num = input()
        div5=int(num)%5
        div3=int(num)%3

        if div5==0 and div3==0:
            print('Fizzbuzz')
            print('Try again?')



        elif div5==0:
            print('Buzz')

        elif div3==0:
            print('Fizz')

        else:
            print("Sorry" + num + " is not a fizz, fizzbuzz or buzz. Try again")


fizzBuzz()