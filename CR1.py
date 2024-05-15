def addnumbers():
    FirstNumber= float(input('Enter the first number:\n') )
    SecondNumber= float(input('Enter the second number:\n') )
    print('The sum of',FirstNumber, 'and', SecondNumber, 'is', FirstNumber+SecondNumber )
    print(FirstNumber, 'minus', SecondNumber, 'is', FirstNumber - SecondNumber )


def multiplyDivide():
    FirstNumber= float(input('Enter the first number:\n') )
    SecondNumber= float(input('Enter the second number:\n') )
    print('The multiplication of',FirstNumber, 'and', SecondNumber, 'is', FirstNumber*SecondNumber )
    print(FirstNumber, 'divided by', SecondNumber, 'is', FirstNumber/SecondNumber )


addnumbers()
multiplyDivide()
