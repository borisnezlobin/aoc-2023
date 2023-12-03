import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
numbers = "0123456789"
not_symbols = " 0123456789."

# returns a list of tuples, each tuple is a number, the index of the number, and the length of the number
def find_nums_in_str(s: str) -> list[(int, int, int)]:
    nums = []
    for i in range(len(s)):
        start = i
        if s[i] in numbers:
            full_num = 0
            while True:
                if i < len(s) and s[i] in numbers:
                    new_c = s[i]
                    full_num = full_num * 10 + int(new_c)
                    s = s[:i] + " " + s[i + 1:]
                    i += 1
                else:
                    break
            nums.append((full_num, start, len(str(full_num))))
    return nums

def solve(s: str) -> int:
    lines1 = s.splitlines()
    lines1 = ["." * len(lines1[0]), *lines1, "." * len(lines1[0])]
    lines = []
    for line in lines1:
        lines.append("." + line + ".")
    
    sum = 0
    # basically, I added a line of "." on top and bottom, and a "." to the start and end of each line
    # it made it easier to check if a number was adjacent to a symbol
    for i in range(1, len(lines) - 1):
        line = lines[i]
        for j in range(1, len(line) - 1):
            if j > len(line) - 1:
                break
            c = line[j]
            if c == "*":
                valid_nums = []
                # check surrounding 7x3 area for numbers
                top_nums = find_nums_in_str(lines[i - 1][j - 3:j + 4])
                left_nums = find_nums_in_str(lines[i][j - 3:j])
                right_nums = find_nums_in_str(lines[i][j + 1:j + 4])
                bottom_nums = find_nums_in_str(lines[i + 1][j - 3:j + 4])
                
                # now, we want to check if any of these numbers are adjacent to a symbol (using the offsets and lengths)
                for num in top_nums:
                    if num[2] == 1 and num[1] in [2, 3, 4]:
                        valid_nums.append(num)
                    elif num[2] == 2 and num[1] in [1, 2, 3, 4]:
                        valid_nums.append(num)
                    elif num[2] == 3 and num[1] in [0, 1, 2, 3, 4]:
                        valid_nums.append(num)
                for num in left_nums:
                    if num[1] + num[2] == 3:
                        valid_nums.append(num)
                
                for num in right_nums:
                    if num[1] == 0:
                        valid_nums.append(num)
                for num in bottom_nums:
                    if num[2] == 1 and num[1] in [2, 3, 4]:
                        valid_nums.append(num)
                    elif num[2] == 2 and num[1] in [1, 2, 3, 4]:
                        valid_nums.append(num)
                    elif num[2] == 3 and num[1] in [0, 1, 2, 3, 4]:
                        valid_nums.append(num)

                if len(valid_nums) == 2:
                    sum += valid_nums[0][0] * valid_nums[1][0]


        # print(line)
    print(sum)

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
