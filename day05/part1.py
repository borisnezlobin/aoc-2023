import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    seeds = lines[0].split(": ")[1].split(" ")
    seed_has_been_mapped = [False] * len(seeds)

    for i in range(0, len(seeds)):
        seeds[i] = int(seeds[i])

    # ho li fuk how do I solve this
    # uh
    # OHHH ok so basically you do this:
    for i in range(3, len(lines)):
        if ":" in lines[i]:
            for j in range(0, len(seeds)):
                seed_has_been_mapped[j] = False
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
    
    # this is the important part I think
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
