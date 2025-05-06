# calculator.py
def add(numbers: str) -> str:
    if not numbers:
        return "0"
    parts = numbers.split(",")
    total = sum(float(p) for p in parts)
    return str(total)

