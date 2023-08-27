Text = input("Greting: ").strip().lower()

first_char = Text[0]
hello = Text[ 0: 5]

match hello:
    case "hello":
        print("$0")
    case _:
        match first_char:
            case "h":
                print("$20")
            case _:
                print("$100")
