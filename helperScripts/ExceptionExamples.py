class BadUserInput(Exception):
    pass

class Fun():
    def haveFun(self, string):
        if string == 'yes':
            print("yay, we had fun")
        elif string == 'no':
            print("something else")
        else:
            raise BadUserInput

def main():
    fun = Fun()
    userInput = input()
    fun.haveFun(userInput)

if __name__ == '__main__':
    main()