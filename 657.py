def power(a: float, n: int) -> float:
    if n < 0:
        a = 1.0 / a
        n = -n
    result = 1.0
    for _ in range(n):
        result *= a
    return result
def main() -> None:
    try:
        while True:
            raw_a = input().strip()
            if not raw_a:
                continue
            a = float(raw_a)
            n = int(input().strip())
            print(power(a, n))
    except EOFError:
        pass
if __name__ == "__main__":
    main()