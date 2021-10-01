number=0
while number <100:
    if number%10==1:
        if number ==71:
            print(number + 1, 'процента')
        elif number %12==11:
            print(number+1, 'процентов ')
        elif number %12!=11:
            print(number+1, 'процента ')
    elif number%10==2:
        if number % 13 == 12:
            print(number + 1, 'процентов ')
        else:
            print(number+1, 'процента ')
    elif number % 10 == 3:
        if number ==83:
            print(number + 1, 'процента ')
        elif number % 14 == 13:
            print(number + 1, 'процентов ')
        else:
            print(number + 1, 'процента ')
    elif number % 11 == 10:
        print(number + 1, 'процентов ')
    elif number %10==0:
        print(number+1, 'процент ')
    else:
        print(number+1, 'процентов ')
    number = number + 1