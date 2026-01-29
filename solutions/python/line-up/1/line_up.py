def line_up(name: str, number: int) -> str:
    match number % 10:
        case 1:
            match number % 100:
                case 11:
                    ordinal = "th"
                case _:
                    ordinal = "st"
        case 2:
            match number % 100:
                case 12:
                    ordinal = "th"
                case _:
                    ordinal = "nd"
        case 3:
            match number % 100:
                case 13:
                    ordinal = "th"
                case _:
                    ordinal = "rd"
        case _:
            ordinal = "th"

    return f"{name}, you are the {number}{ordinal} customer we serve today. Thank you!"
