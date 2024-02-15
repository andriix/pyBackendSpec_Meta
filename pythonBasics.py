print("Hello. Input http status:")
stat = float(input())

match stat:
    case 200 | 201:
        print("successs")
    case 400:
        print("bad")
    case 500:
        print("error")
    case _:
        print("unknown")

