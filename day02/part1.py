import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    
    sum = 0
    for line in lines:
        id = int(line.split(':')[0].split(' ')[1])
        games = line.split(':')[1].split(';')
        count_it = True
        for game in games:
            colors = game.split(', ')
            red = green = blue = 0
            for color in colors:
                color = color.strip()
                if(color.split(' ')[1] == 'red'):
                    red = max(red, int(color.split(' ')[0]))
                elif(color.split(' ')[1] == 'green'):
                    green = max(green, int(color.split(' ')[0]))
                elif(color.split(' ')[1] == 'blue'):
                    blue = max(blue, int(color.split(' ')[0]))
            if red > 12 or green > 13 or blue > 14:
                count_it = False
                break
        if count_it:
            sum += id
        else:
            print("not counting game ", id)
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
