import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
# 251545177 is NOT the answer
mapping = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}

def solve(s: str) -> int:
    lines = s.splitlines()
    hands = []
    for line in lines:
        if line == '':
            continue
        # so we can give each hand a "score"
        # five of a kind always beats four of a kind, always beats three of a kind, etc.
        hand = line.split()[0]
        scores = [0] * 13
        jacks = 0
        for i in range(len(hand)):
            if hand[i] == 'J':
                jacks += 1
            else:
                scores[mapping[hand[i]] - 2] += 1
        
        print(hand, scores, jacks)
        
        # now determine if the hand is five in a row, four in a row, etc.
        first_digit = 0
        if max(scores) == 5 or max(scores) + jacks == 5:
            # five of a kind
            first_digit = 6
        elif max(scores) + jacks == 4:
            # four and one
            first_digit = 5
        elif max(scores) + jacks == 3:
            if (
                (scores.count(3) == 1 and scores.count(2) == 1) or # 0 jacks
                (scores.count(2) == 2 and jacks == 1) # 1 jack
            ):
                # three and two
                first_digit = 4
            else:
                # three, one, and one
                first_digit = 3
        elif scores.count(2) * 2 + jacks == 4:
            # two, two, and one
            first_digit = 2
        elif max(scores) + jacks == 2:
            # two, one, one, one
            first_digit = 1
        elif max(scores) == 1 and scores.count(1) == 5:
            # one, one, one, one, one
            first_digit = 0

        number = [first_digit]
        for i in hand:
            # if mapping[i] < 10:
            #     number = number * 10
            number.append(mapping[i])
        # print(hand + ":", number)

        hands.append((number, int(line.split()[1]), hand))

    hands.sort()
    print(hands)

    sum = 0
    for i in range(len(hands)):
        sum += hands[i][1] * (i + 1)
    
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
