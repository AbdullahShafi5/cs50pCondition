def main():
    greet_user = input("Greeting:")
    greet_user = greet_user.strip()
    greetings(greet_user)

def greetings(x):
    case_1  = "hello"
    case_1 = case_1.lower()
    x = x.lower()
    if x == case_1:
        print("$0")
    elif x.startswith("hello"): 
        print("$0")
    elif x.startswith("h") and x != "hello":
        print("$20")
    else:
        print("$100")

main()