

x = 10
try:
    print(x)
except NameError:
    print("Please define x first.")
else:
    print("Your code has been succesfully executed")
finally:
    print("The 'try except' is finished")
