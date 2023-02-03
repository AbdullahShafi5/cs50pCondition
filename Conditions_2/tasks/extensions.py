#main function 
def main():
    user_inp = input("File name:")
    user_inp = user_inp.strip()
    extensions(user_inp)
    
#checking for the extension 
def extensions(n):
    n = n.lower()
    case_1 = ".gif"
    case_2 = ".jpg"
    case_3 = ".jpeg"
    case_4 = ".png"
    case_5 = ".pdf"
    case_6 = ".txt"
    case_7 = ".zip"

    if case_1 in n:
        print("image/gif")

    elif case_2 in n or case_3 in n:
        print("image/jpeg")

    elif case_4 in n:
        print("image/png")

    elif case_5 in n:
        print("application/pdf")

    # elif n.lower() == case_5.lower():
    #     print("image/pdf")

    elif case_6 in n:
        print("text/plain")

    elif case_7 in n:
        print("application/zip")
    
    else:
        print("application/octet-stream")

main()