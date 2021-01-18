

class UserInput:

    def __init__(self):
        self.a = 5
        self.b = None

    def get_user_input(self):
        x = input('Give me a value: ')
        self.a = 15
        return x

    def print_user_input(self, a=None, b=None):
        print(a)
        print(self.a)
        print(b)


if __name__ == "__main__":
    print('Hi')
    ui = UserInput()
    # x = ui.get_user_input()
    ui.print_user_input()

