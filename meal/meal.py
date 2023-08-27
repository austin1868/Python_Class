def main():
    time_str = input('What time is it?' )
    time_dec = convert(time_str)
    #print(time_dec)

    if 7 <= time_dec <= 8:
        print("breakfast Time")
    elif 12 <= time_dec <= 13:
        print("lunch Time")
    elif 18 <= time_dec <= 19:
        print("dinner Time")

def convert(time_str):
    hours, minutes = time_str.split(":")
    hours = int(hours)
    minutes = int(minutes)
    mth = minutes / 60
    time_dec = hours + mth
    return(time_dec)

if __name__ == "__main__":
    main()