import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

valid_strings = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
]

print(valid_strings[16])

def solve(s: str) -> int:
    lines = s.splitlines()
    # for line in lines:
        # print(line)
    sum = 0
    for line in lines:
        first = -1
        last = -1
        for i in range(0, len(line)):
            for j in range(0, len(valid_strings)):
                if(len(valid_strings[j][0]) < len(line) + 1 - i):
                    if(line[i:i + len(valid_strings[j][0])] == valid_strings[j][0]):
                        if(first == -1):
                            first = valid_strings[j][1]
                        last = valid_strings[j][1]
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
