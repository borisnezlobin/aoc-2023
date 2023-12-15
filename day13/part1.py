import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'fake_input.txt')

def find_vertical_reflection(pattern: str) -> int:
    equal_cols = {}
    lines = pattern.split("\n")
    cols = [""] * len(lines[0])
    for i in range(0, len(lines[0])):
        equal_cols[i] = []
        for j in range(0, len(lines)):
            cols[i] += lines[j][i]
    
    print(cols)

    for i in range(0, len(cols)):
        for j in range(i + 1, len(cols)):
            if cols[i] == cols[j]:
                equal_cols[i].append(j)
                equal_cols[j].append(i)
    
    print(equal_cols)



def solve(s: str) -> int:
    patterns = s.split("\n\n")

    for pattern in patterns:
        print(pattern, end="\n=====\n")
        find_vertical_reflection(pattern)
    
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
