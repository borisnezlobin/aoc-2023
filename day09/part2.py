import os.path
from typing import List

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def common_step(nums: List[int]) -> int:
    differences = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    if nums.count(max(nums)) == len(nums):
        return nums[0]

    else:
        return nums[0] - common_step(differences)


def solve(s: str) -> int:
    lines = s.splitlines()
    sum = 0
    for line in lines:
        nums = [int(n) for n in line.split()]
        sum += common_step(nums)
    print(sum)
    return 0

INPUT_S = '''\

'''
EXPECTED = 0


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        solve(f.read())
    return 0


if __name__ == '__main__':
    main()