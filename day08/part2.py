import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

nodes = {}

# idk wtf "scaler" is, but that's where I got this lcm code from
# yeah it is NOT efficient enough to find the LCM for my input (ended up being ~15 trillion)
# so I had to use an online tool but whatever
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def solveForOneString(s: str, start: str) -> int:
    print("Solving for", start)
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
    next_node = start

    while next_node[-1] != 'Z':
        direction_to_go = directions[steps % len(directions)]
        left, right = nodes[next_node]
        if direction_to_go == 'L':
            next_node = left
        elif direction_to_go == 'R':
            next_node = right
        else:
            raise Exception('invalid direction')
        steps += 1
    
    print("Start", start, "has score", steps)

    return steps

def solve(s: str) -> int:
    lines = s.splitlines()
    starts = []

    for i in range(1, len(lines)):
        line = lines[i]
        if len(line) == 0:
            continue

        # in the format "name = (left, right)"
        node_name = line.split(' = ')[0]
        if node_name[-1] == "A":
            starts.append(node_name)
    
    print("Starting at", starts)

    scores = []
    for start in starts:
        scores.append(solveForOneString(s, start))
    
    # find lcm of scores
    lcm_ = scores[0]
    for i in range(1, len(scores)):
        lcm_ = lcm(lcm_, scores[i])

    print("LCM is", lcm_)
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
