def fizzBuzz():
    x = ""
    for i in range(1,101):
        if (i % 3 == 0):
            x+= "Fizz "
        elif (i % 5 == 0):
            x+= "Buzz "
        else:
            x+= (str(i) + " ")
    return x
