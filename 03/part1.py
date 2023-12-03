import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
numbers = "0123456789"
not_symbols = " 0123456789."

def solve(s: str) -> int:
    lines1 = s.splitlines()
    lines1 = ["." * len(lines1[0]), *lines1, "." * len(lines1[0])]
    lines = []
    for line in lines1:
        lines.append("." + line + ".")
    
    sum = 0
    # basically, I added a line of "." on top and bottom, and a "." to the start and end of each line
    # it made it easier to check if a number was adjacent to a symbol
    for i in range(1, len(lines) - 1):
        line = lines[i]
        for j in range(1, len(line) - 1):
            if j > len(line) - 1:
                break
            c = line[j]
            num_is_ajacent_to_symbol = False
            if c in numbers:
                full_num = 0
                while True:
                    if line[j] in numbers:
                        new_c = line[j]
                        full_num = full_num * 10 + int(new_c)
                        if (lines[i - 1][j] not in not_symbols
                        or lines[i + 1][j] not in not_symbols
                        or lines[i][j- 1] not in not_symbols
                        or lines[i][j + 1] not in not_symbols
                        or lines[i - 1][j - 1] not in not_symbols
                        or lines[i - 1][j + 1] not in not_symbols
                        or lines[i + 1][j - 1] not in not_symbols
                        or lines[i + 1][j + 1] not in not_symbols):
                            num_is_ajacent_to_symbol = True
                        line = line[:j] + " " + line[j + 1:]
                        j += 1
                    else:
                        break
                if num_is_ajacent_to_symbol:
                    print("adding ", full_num)

                    # just a check that all numbers are less than three digits in length, necessary for my cursed solution to part 2
                    if(full_num > 999):
                        print("BIG NUMBER: " + full_num)
                    sum += full_num

        print(line)
    print(sum)

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
