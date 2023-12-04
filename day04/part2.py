import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    copies = {}
    for i in range(1, len(lines) + 1):
        copies[i] = 1
    for i in range(0, len(lines)):
        line = lines[i]
        print(line)
        winning_numbers = {}
        total = 0
        line = line.split(": ")[1]
        winners = line.split(" | ")[0]
        numbers = line.split(" | ")[1]

        for winner in winners.split(" "):
            if winner.strip() != "":
                winning_numbers[winner.strip()] = 1
        
        for number in numbers.split(" "):
            if number.strip() == "":
                continue
            if number.strip() in winning_numbers:
                total += 1
        
        print(total)
        for j in range(i + 1, i + 1 + total):
            copies[j + 1] += copies[i + 1]
        print(copies)

    sum = 0
    for i in range(1, len(lines) + 1):
        sum += copies[i]

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
