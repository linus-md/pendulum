import re
from tabulate import tabulate


def parse(log):
    """
    This function parses Singular Gröbner basis log output and saves the data
    in a useful format. The input is a string containing the log output.

    The log: '''[65535:4]2(3)s(2)sss3(3)s(4)s(5)s(7)s4(9)s(11)--
    s(12)s(15)----5---s(10)s(11)s(14)-----6--------'''
    generates the following output:
    `[[2, 4, 0], [3, 4, 0], [4, 3, 6], [5, 3, 8], [6, 0, 8]]`.
    """
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

        pos = [pos[0]]
        pos += [pos[i] for i in range(1, len(pos)) if pos[i] - pos[i-1] != 1]
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
