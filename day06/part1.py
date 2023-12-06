import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()

    error = 1

    for i in range(len(distances)):
        length = int(distances[i])
        time = int(times[i])
        for j in range(0, time):
            if j * (time - j) > length:
                print(j, length, time)
                print(time - (2 * j))
                error *= time - (2 * j) + 1
                break
    
    print("the answer is", error)

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
