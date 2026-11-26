def calculate_deposit(n: float, p: float, m: int) -> float:
    return n + n * (p / 100) * m
def main() -> None:
    try:
        while True:
            raw_n = input().strip()
            if not raw_n:
                continue
            n = float(raw_n)
            p = float(input().strip())
            m = int(input().strip())
            print(f"{calculate_deposit(n, p, m):.2f}")
    except EOFError:
        pass
if __name__ == "__main__":
    main()