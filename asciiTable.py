def main():
    LOWER = 33
    UPPER = 127
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))
    num = get_number(LOWER,UPPER)
    print("The character for {} is {:>3}".format(num, chr(num)))
    for i in range(LOWER, UPPER, 1):
     print("{} {:>3}".format(i, chr(i)))



def get_number(LOWER,UPPER):
    try:
        inputNum = int(input("Enter a number between {}-{}: ".format(LOWER, UPPER)))
        while inputNum not in range(LOWER,UPPER):
            inputNum = int(input("Enter a number between {}-{}: ".format(LOWER, UPPER)))
    except ValueError:
        print("not a valid integer") #help here
    return inputNum

main()

