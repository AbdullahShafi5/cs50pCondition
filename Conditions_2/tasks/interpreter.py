
def main():
    user_inp = input("enter :")
    user_inp = user_inp.strip()
    calculation(user_inp)

def calculation(x):
    term_1, operator, term_2 = x.split() #breaking all the terms apart
    term_1 = float(term_1)
    term_2 = float(term_2)    
    p = "+"
    m = "-"
    mlt = "*"
    d = "/"
    if p in operator:
        result =  term_1 + term_2
        print(result)
    elif m in operator: 
        result = term_1 - term_2
        print(result)
    elif mlt in operator:
        result = term_1*term_2
        print(result)
    elif d in operator:
        result = term_1/term_2
        print(round(result,1))
    else:
        print("something went wrong")

main()