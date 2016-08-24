def get_name():
    def main():
        name = input("please enter your name: ")
        while name == "":
            name = input("please enter your name: ")
        print_loop(name)

    return main


main = get_name()

def print_loop(name):
    print(name[::2])
# i dont know what this thing is asking for me to do


main()
