import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    sum = 0
    for line in lines:
        print(line)
        winning_numbers = {}
        score = 0
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
                if score == 0:
                    score = 1
                else:
                    score *= 2
        
        sum += score
        print(score)
    
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
