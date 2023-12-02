import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    
    sum = 0
    for line in lines:
        games = line.split(':')[1].split(';')
        red = green = blue = 0
        for game in games:
            colors = game.split(', ')
            for color in colors:
                color = color.strip()
                if(color.split(' ')[1] == 'red'):
                    red = max(red, int(color.split(' ')[0]))
                elif(color.split(' ')[1] == 'green'):
                    green = max(green, int(color.split(' ')[0]))
                elif(color.split(' ')[1] == 'blue'):
                    blue = max(blue, int(color.split(' ')[0]))
        print(red, green, blue)
        sum += red * green * blue
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
