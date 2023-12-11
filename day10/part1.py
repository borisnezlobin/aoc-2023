import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'fake_input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    # row elements have the format (left, top, right, bottom)
    graph = []
    scores = []
    start = (-1, -1)
    for i in range(len(lines)):
        line = lines[i]
        row = []
        scores_row = []
        for j in range(len(line)):
            value = (False, False, False, False)
            if line[j] == 'F':
                value = (False, False, True, True)
            elif line[j] == '7':
                value = (True, False, False, True)
            elif line[j] == 'L':
                value = (False, True, True, False)
            elif line[j] == 'J':
                value = (True, True, False, False)
            elif line[j] == "-":
                value = (True, False, True, False)
            elif line[j] == "|":
                value = (False, True, False, True)

            if line[j] == 'S':
                start = (i, j)
                value = (True, True, True, True)
            
            if value == (False, False, False, False):
                scores_row.append(-1)
            else:
                scores_row.append(0)
            
            row.append(value)
        graph.append(row)
        scores.append(scores_row)
    
    # now we have a graph, we want to assign scores to everything reachable from start
    new_start_tuple = [False, False, False, False]
    if graph[start[0]][start[1] - 1][2]:
        new_start_tuple[0] = True
    if graph[start[0] - 1][start[1]][3]:
        new_start_tuple[1] = True
    if graph[start[0]][start[1] + 1][0]:
        new_start_tuple[2] = True
    if graph[start[0] + 1][start[1]][1]:
        new_start_tuple[3] = True

    # turn list into tuple
    new_start_tuple = tuple(new_start_tuple)

    visited = set()

    graph[start[0]][start[1]] = new_start_tuple
    print("start tuple", new_start_tuple)
    to_visit = [(start[0], start[1], 1)]
    while len(to_visit) > 0:
        new_to_visit = []
        while len(to_visit) > 0:
            next = to_visit.pop()
            # print("now visiting", next)
            if scores[next[0]][next[1]] == 0:
                scores[next[0]][next[1]] = next[2]
                if graph[next[0]][next[1]][0]:
                    new_to_visit.append((next[0], next[1] - 1, next[2] + 1))
                if graph[next[0]][next[1]][1]:
                    new_to_visit.append((next[0] - 1, next[1], next[2] + 1))
                if graph[next[0]][next[1]][2]:
                    new_to_visit.append((next[0], next[1] + 1, next[2] + 1))
                if graph[next[0]][next[1]][3]:
                    new_to_visit.append((next[0] + 1, next[1], next[2] + 1))
                
                if (next[0], next[1]) in visited:
                    break
                    
                visited.add((next[0], next[1]))
        for i in range(len(scores)):
            for j in range(len(scores[i])):
                if scores[i][j] == -1:
                    print(' ' * 5, end='')
                else:
                    print(scores[i][j], end=(' ' * (4 - len(str(scores[i][j]))) + ' '))
            print()
        print("\n==========")
        to_visit = new_to_visit
    
    m = 0
    for i in range(len(scores)):
        for j in range(len(scores[i])):
            if scores[i][j] > m:
                m = scores[i][j]
    
    print("max score", m - 1)
    
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
