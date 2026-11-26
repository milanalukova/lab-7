def permute(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    current: list[int] = []
    used = [False] * len(nums)
    def backtrack() -> None:
        if len(current) == len(nums):
            result.append(current.copy())
            return
        for i in range(len(nums) - 1, -1, -1):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False
    backtrack()
    return result
def main() -> None:
    try:
        while True:
            raw = input().strip()
            if not raw:
                continue
            nums = list(map(int, raw.split()))
            print(permute(nums))
    except EOFError:
        pass
if __name__ == "__main__":
    main()