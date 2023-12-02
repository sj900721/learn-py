import pyjokes

def greeting_func(name):
    print("Hello,", name)
    print("Here is a joke for you:\n", pyjokes.get_joke())
