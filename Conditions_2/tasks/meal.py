def main():
    user_time = input("what time is it? ")
    # user_time = user_time.strip()
    convert(user_time)
        
def convert(time):
    user_time_hour, user_time_minutes = time.split(":")
    minutes = float(user_time_minutes)/60
    result_time = minutes + float(user_time_hour)

    if result_time >= 7 and result_time <= 8: 
        print("breakfast time")

    elif result_time >= 12 and result_time <= 13:
        print("lunch time")

    elif result_time>= 18 and result_time <= 19:
        print("dinner time") 
    return result_time

if __name__ == "__main__":
    main()
