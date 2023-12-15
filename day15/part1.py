import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def HASH(s: str) -> int:
    h = 0
    for c in s:
        # get ascii value of c
        ascii = ord(c)
        print(ascii, c)
        h += ascii
        h *= 17
        h = h % 256

    return h

def solve(s: str) -> int:
    nums = s.splitlines()[0].split(',')

    sum = 0
    for num in nums:
        sum += HASH(num)
    
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
