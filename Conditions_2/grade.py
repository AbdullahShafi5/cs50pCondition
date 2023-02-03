score = int(input("Score:"))

if score >= 90 and  score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
elif score >= 60 and score < 70:
    print("Grade D")

else:
    print("Grade F")

# can be written in this way as well. 
if  90<= score <= 100:
    print("A")
elif 80<= score < 90:
    print("B")
else:
    print("F")


#more sophisticated and straight way 
if score >=  90:
    print('A')
elif score >= 80:
    print("B")
else:
    print("GTFO")