# add your code here

def isFizz(num:int) -> bool:
    """
    function to determine if the given number is evenly divisible by 3
    param num: the number to be tested
    return: True if the number is evenly divisible, False if it is not
    """
    return num % 3 == 0

def isBuzz(num:int) -> bool:
    """
    function to determine if the given number is evenly divisible by 5
    param num: the number to be tested
    return: True if the number is evenly divisible, False if it is not
    """
    return num % 5 == 0

def main() -> None:
    # create an iterator from 1 to 100
    numbers = range(1, 101)

    # loop through the iterator and test each number
    for num in numbers:
        # if the number is evenly divisble by 3 and 5 print 'FizzBuzz'
        if isFizz(num) and isBuzz(num):
            print('FizzBuzz')
        # if the number is evenly divisible by 3 print 'Fizz'
        elif isFizz(num):
            print('Fizz')
        # if the number is evenly divisible by 5 print 'Buzz'
        elif isBuzz(num):
            print('Buzz')
        # Otherwise just print the number
        else:
            print(num)

# boilerplate code to run the main() function when 
# this script is called from the command line.
if __name__ == "__main__":
    main()
