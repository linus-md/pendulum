import re
from tabulate import tabulate

def parse(log):
    log = log.split(']')[1]

    def find_standalone_numbers(log):
        open_paren = False
        pos = []
        i = 0
        while i < len(log):
            char = log[i]
            if char == '(':
                open_paren = True
            elif char == ')':
                open_paren = False
            elif char.isdigit() and not open_paren:
                start = i
                while i < len(log) and log[i].isdigit():
                    i += 1
                end = i
                if (start == 0 or not log[start-1].isdigit()) and \
                   (end == len(log) or not log[end].isdigit()):
                    pos.extend(range(start, end))
                continue
            i += 1

        # Adjust pos to remove consecutive elements which are part of the same number
        pos = [pos[0]] + [pos[i] for i in range(1, len(pos)) if pos[i] - pos[i-1] != 1]
        return pos

    # Find substrings
    pos = find_standalone_numbers(log)
    sub_strings = [log[pos[i]:pos[i+1]] for i in range(len(pos)-1)]
    sub_strings.append(log[pos[-1]:])


    # Evalute each substring
    vals = []
    for sub in sub_strings:
        s = sub.count('s')
        z = sub.count('-')
        digits = re.findall(r'\d+', sub)
        if digits:
            deg = int(digits[0])
        else:
            deg = 0
        vals.append([deg, s, z])

    headers = ['deg', 'nonzero', 'zero']
    return vals, headers


if __name__ == '__main__':
    input = input("Enter your input: ")
    vals, headers = parse(input)
    print(tabulate(vals, headers=headers))