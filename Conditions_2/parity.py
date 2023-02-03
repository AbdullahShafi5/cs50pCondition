x = int(input("X:"))

if x%2 == 0:
    print("even")
else:
    print("odd")


#using main function | elegant 
def main():
    x = int(input("enter the number:"))
    if is_even(x):
        print("Even")
    else:
        print("odd")


def is_even(n):
    return n % 2 == 0 #most elegant way just return the question
    return True if n % 2 == 0 else False #wtf is this | pythonic way
    if n % 2 == 0: #general way 
        return True
    
    # else:  #don't have to retun false since it will retun false by default if ans is not True
    #     return False

main()
