#   compatible python 2.7.x and up

'''
    This program coverts inputted HH:MM time to human readable time
    Uses basic dictionaries and string returns
'''


#   keys and dictionaries
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
tens = ["teen", "twenty", "thirty", "forty", "fifty"]
misc = ["thir", "four", "fif"]
misc2 = ["quarter", "half", "o\' clock"]


def towords(t):
    if t <= 12:
        return ones[t-1]
    elif t in range(13, 16):
        return misc[t-13]+tens[0]
    elif t in range(16, 20):
        if t is 18:
            return "eighteen"
        else:
            return ones[t-11]+tens[0]
    else:
        if t%10 is 0:
            return tens[int(t / 10) - 1]
        else:
            return tens[int(t/10)-1]+" "+ones[t%10-1]


def minner():
    if min is 1:
        return "minute"
    else:
        return "minutes"


def printer(hr, min):
    if min < 0 or min > 60 or hr < 1 or hr > 12:
        print("Invalid Input")
    else:
        if min is 0:
            print(towords(hr),misc2[2])
        elif min < 30:
            str1 = minner()
            if min is 15:
                print(misc2[0], "past", towords(hr))
            else:
                print(towords(min), str1, "past", towords(hr))
        elif min is 30:
            print(misc2[1], "past", towords(hr))
        else:
            if min is 45:
                if hr is 12:
                    print(misc2[0], "to", "one")
                else:
                    print(misc2[0], "to", towords(hr+1))
            else:
                min = 60 - min
                str1 = minner()
                if hr is 12:
                    print(towords(min), "to", "one")
                else:
                    print(towords(min), str1, "to", towords(hr+1))


def main(x):
    hr, min = map(int, x.split())
    printer(hr, min)

if __name__ == '__main__':
    main(input())
