import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# 619902767 648714498 3762874676 148318192 1545670780 343889780 4259893555 6139816 3980757676 20172062 2199623551 196958359


def solve(s: str) -> int:
    lines = s.splitlines()
    seeds1 = lines[0].split(": ")[1].split(" ")

    def generate_seeds(seeds1):
        for i in range(0, len(seeds1), 2):
            print("seeding " + str(seeds1[i]) + " to " + str(seeds1[i + 1]))
            for j in range(0, int(seeds1[i + 1])):
                yield int(seeds1[i]) + j

    seeds = list(generate_seeds(seeds1))
    print(seeds)
    seed_has_been_mapped = [False] * len(seeds)

    for i in range(3, len(lines)):
        if ":" in lines[i]:
            seed_has_been_mapped = [False] * len(seeds)
            print("==========")
            continue
        
        if len(lines[i]) == 0:
            continue
        end, start, rng = lines[i].split(" ")
        start = int(start)
        end = int(end)
        rng = int(rng)

        for j in range(0, len(seeds)):
            seed = seeds[j]
            if not seed_has_been_mapped[j] and start <= seed <= start + rng:
                seed_has_been_mapped[j] = True
                seeds[j] = end + (seed - start)
        print(seeds)
    
    print(min(seeds))

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
