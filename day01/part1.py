import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    sum = 0
    for line in lines:
        first = -1
        last = -1
        for char in line:
            if char.isdigit():
                if(first == -1):
                    first = int(char)
                last = int(char)
        sum += first * 10 + last
    print(sum)
    return 0

INPUT_S = '''\

'''
EXPECTED = 0


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
