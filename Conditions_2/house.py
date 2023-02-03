name = input("What's your name?")

if name == "Harry" or name == "python" or name =="cpp":
    print("Gryffindor")
elif name == "Hermione":
    print("Hamelton")
elif name == "Ron":
    print("uganda")
else:
    print(f"who the fuck is {name}? ")


#doing this using match statement | same as if (case ) else( case _ ) 

match name:
    case "Raven" | "Rolins" | "semuel": # | same as  " or "
        print("draginton")
    case "blacku":
        print("kalabari")
    case _:
        print(f"who the fuck is {name}? ")