# match-case statements

seat_type=input("Enter seat type(sleeper/Ac/general/luxury)\n").lower()

match seat_type:
    case "sleeper":
        print("sleeper is available")
    case "ac":
        print("AC is available")
    case "general":
        print("general is available")
    case "luxury":
        print("luxury is available")
    case _:
        print("invalid seat type")