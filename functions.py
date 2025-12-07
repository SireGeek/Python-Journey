def greet(name: str, greeting: str) -> str:    
    message = f"{greeting}, {name}!"
    print(message)
    return message

greeting = "Hello"

name = input('Enter your name: ')
greet(name, greeting)
