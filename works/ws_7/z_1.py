class Show:
    def __init__(self, str):
        self.str = str

    def print_str(self):
        print(self.str)

str1 = Show('hello')
str1.print_str()
print("====")
print_str(str1)