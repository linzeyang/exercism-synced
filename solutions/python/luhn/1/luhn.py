class Luhn:
    def __init__(self, card_num: str) -> None:
        self._raw = card_num.replace(" ", "")

    def valid(self) -> bool:
        if len(self._raw) <= 1 or not self._raw.isdigit():
            return False

        digits = [int(char) for char in self._raw]

        summ = 0

        for i in range(1, len(digits) + 1):
            if i % 2 == 1:
                summ += digits[-i]
            else:
                digit = digits[-i] * 2
                if digit > 9:
                    digit -= 9
                summ += digit

        return summ % 10 == 0
                
