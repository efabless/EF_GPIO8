class item ():
    x=0 
    y=0
    def __init__(self, name="item"):
        self.a = 0
        self.b = 0

    def add(self):
        self.a = self.x + self.y
        return self.a

class sub_item(item):

    def __init__(self, name="sub_item"):
        super().__init__(name)
    
    def sub(self):
        self.b = self.x - self.y
        return self.b


item1 = item()
item1.x = 3
item1.y = 5

print(item1.add())

sub_item1 = sub_item()
sub_item1.x = 10
sub_item1.y = 5
print(sub_item1.sub())


def print_hello_decorator(function):
    def wrapper(num):
        print("Hello!")
        num_P_1 = num + 1
        print("Hello again!")
        return function(num_P_1)
    
    return wrapper

@print_hello_decorator
def test_function(num):
    print("This is the test function")
    return num+1


print(test_function(2))

print((" GPIOs out enable = %s , GPIOs output =  %s , GPIOs input = %s", 5, 9, 10))





