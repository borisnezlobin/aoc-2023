import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

mult = 1000000 - 1

def solve(s: str) -> int:
    print(s)
    lines = s.splitlines()

    empty_rows = [0] * len(lines)
    empty_cols = [0] * len(lines[0])
    galaxies = []

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                galaxies.append((i, j))
            else:
                empty_rows[i] += 1
                empty_cols[j] += 1
    
    for i in range(len(empty_rows)):
        if empty_rows[i] == len(lines[0]):
            empty_rows[i] = 1
        else:
            empty_rows[i] = 0

    for j in range(len(empty_cols)):
        if empty_cols[j] == len(lines):
            empty_cols[j] = 1
        else:
            empty_cols[j] = 0
    
    print("rows", empty_rows)
    print("cols", empty_cols)
    print(galaxies)

    # count distances between galaxies
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            dist = 0
            dist += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            min_row = min(galaxies[i][0], galaxies[j][0])
            max_row = max(galaxies[i][0], galaxies[j][0])
            dist += (empty_rows[min_row:max_row + 1].count(1) * mult)
            min_col = min(galaxies[i][1], galaxies[j][1])
            max_col = max(galaxies[i][1], galaxies[j][1])
            dist += (empty_cols[min_col:max_col + 1].count(1) * mult)

            print(galaxies[i], galaxies[j], dist)
            sum += dist

    print(sum)

    # code
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
