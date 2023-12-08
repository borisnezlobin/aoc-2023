import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

nodes = {}

def solve(s: str) -> int:
    lines = s.splitlines()
    directions = lines[0] # a string like 'LLR'

    for i in range(1, len(lines)):
        line = lines[i]
        if len(line) == 0:
            continue

        # in the format "name = (left, right)"
        node_name = line.split(' = ')[0]
        left, right = line.split(' = ')[1].split(', ')
        left = left.replace('(', '')
        right = right.replace(')', '')

        nodes[node_name] = (left, right)
    
    steps = 0
    next_node = 'AAA'

    print(nodes)

    while next_node != 'ZZZ':
        direction_to_go = directions[steps % len(directions)]
        left, right = nodes[next_node]
        if direction_to_go == 'L':
            next_node = left
        elif direction_to_go == 'R':
            next_node = right
        else:
            raise Exception('invalid direction')
        steps += 1
    
    print(steps)

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
