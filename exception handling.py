def div(a,b):
    try:
        return a/b
    except:
        print("Error: cannot divide by zero")
a=div(12,0)
print(a)