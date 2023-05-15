
# time = input("What time is it? ")
# time = time.split(":")
# time = float(time[0]) + (float(time[1])/60)
# time = float(time)

# if 7.0 <= time <= 8.0:
#     print("breakfast time")
# elif 12.0 <= time <= 13.0:
#     print("lunch time")
# elif 18.0 <= time <= 19.0:
#     print("dinner time")
# else:
#     print("None")

def main():
    time = input("What time is it? ")
    time = conver(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        return


def conver(x):
    x = x.split(":")
    x = float(x[0]) + (float(x[1])/60)
    return x

if __name__ == "__main__":
    main()