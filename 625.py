def transform_string(s: str, n: int, m: int) -> str:
    a = s[:m]
    k = sum(1 for c in a if c.isupper())

    if k >= n:
        return s.upper()
    return s
def main() -> None:
    try:
        while True:
            s = input()
            if not s:
                continue
            parts = input().split()
            if len(parts) < 2 or not (parts[0].isdigit() and parts[1].isdigit()):
                continue
            n, m = int(parts[0]), int(parts[1])
            print(transform_string(s, n, m))
    except EOFError:
        pass
if __name__ == "__main__":
    main()