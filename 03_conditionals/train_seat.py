seat = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat:
    case "sleeper":
        print("Sleeper - No AC, beds avail")
    case "ac":
        print("Available")
    case "general":
        print("Cheapest options ")
    case "luxury":
        print("Premium ")
    case _:
        print("Invalid seat type ")