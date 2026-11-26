def solve_animals(n: int, m: int) -> str:
    if m % 2 != 0 or m < 2 * n or m > 4 * n:
        return "NO SOLUTIONS! NO SOLUTIONS!"
    rabbits = (m - 2 * n) // 2
    chickens = n - rabbits
    if chickens < 0 or rabbits < 0:
        return "NO SOLUTIONS!"
    return f"{chickens} {rabbits}"
def main() -> None:
    try:
        while True:
            raw = input().strip()
            if not raw:
                continue
            n, m = map(int, raw.split())
            print(solve_animals(n, m))
    except EOFError:
        pass
if __name__ == "__main__":
    main()