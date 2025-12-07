a, b = 10, 15

try:
    print(a + b)
except TypeError as e:
    print("Type Error occurred")
except Exception as e:
    print("Enter an integer only!")

print ("Execution continues...")