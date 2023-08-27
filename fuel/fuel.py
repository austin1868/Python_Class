

while True:
    try:
        frac = input("fuel remaining: ").split('/')
        if len(frac) != 2:
            raise ValueError
        x = int(frac[0])
        y = int(frac[1])
        pre = x / y*100

        if pre > 100:
            continue
        elif pre >= 99:
            print("F")
        elif pre <= 1:
            print("E")
        else:
            print(f"{pre:.0f}%")
        break
    except ValueError:
        continue

    except ZeroDivisionError:
        continue
