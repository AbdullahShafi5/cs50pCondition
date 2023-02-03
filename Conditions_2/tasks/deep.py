
def main():
    a = input("What is Answer to the Great Question of life, The Universe and Everything? ")
    a = a.strip()
    deep_asking(a)
 
#bullshit xD 
# def deep_asking(a):
#     match a:
#         case "42" | "forty-two" | "forty two" | "Forty Two" | "Forty-Two" | "Forty two":
#             print("Yes")
#         case _:
#             print("No ")         
# main()

def deep_asking(a):
    text_case1  = "forty-two"
    text_case2 = "forty two"
    if a == "42":
        print("yes")
    elif a.lower() == text_case1.lower() or a.lower()==text_case2.lower():
        print("Yes")
    else:
        print("No")

main()