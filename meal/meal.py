def main():
    user_time = input("Enter you time: ")
    user_time = convert(user_time)
    if user_time >= 7 and user_time <= 8:
        print("breakfast time")
    elif user_time >= 12 and user_time <= 13:
        print("lunch time")
    elif user_time >= 18 and user_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = [int(x) for x in time.split(":")]
    minutes = minutes/60
    final_time = hours+minutes

    return final_time

if __name__ == "__main__":
    main()
