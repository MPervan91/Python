x = int(input("Vrijednost za x je: "))

y = int(input("Vrijednost za y je: "))

operation = input("Odaberi matematičku operaciju (+,-,*,/): ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
else:
    print("Niste odabrali valjanu matematičku operaciju.")