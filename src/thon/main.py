from thon.List import List

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def run(code, _stack=()):
    index = 0
    stack = List(_stack)
    while index < len(code):
        char = code[index]
        if char in '0123456789.':
            string = char
            index += 1
            try:
                while code[index] in '0123456789.':
                    string += code[index]
                    index += 1
            except:
                pass
            index -= 1
            stack.push(eval(string))
        elif char == '"':
            string = char
            index += 1
            try:
                while code[index] != '"':
                    string += code[index]
                    index += 1
            except:
                pass
            string += code[index]
            stack.push(eval(string))
        elif char == 'L':
            stack.push([])
        elif char == 'S':
            for item in stack:
                if isinstance(item, list):
                    stack.push(List(item).sum)
                    break
        elif char == 'P':
            for item in stack:
                if isinstance(item, list):
                    stack.push(List(item).product)
        elif char == 'A':
            for l, item1 in enumerate(stack):
                if isinstance(item1, list):
                    break
            else:
                continue
            for n, item2 in enumerate(stack):
                if not isinstance(item2, list):
                    break
            else:
                continue
            stack.push(stack[l] + [stack[n]])
        elif char == 'R':
            for l, item1 in enumerate(stack):
                if isinstance(item1, list):
                    break
            else:
                continue
            for n, item2 in enumerate(stack):
                if not isinstance(item2, list):
                    break
            else:
                continue
            tmp = stack[l].copy()
            tmp.remove(stack[n])
            stack.push(tmp)
        elif char == 'F':
            for item in stack:
                if isinstance(item, (list, str)):
                    stack.push(List(item).repeat)
                    break
        elif char in 'qwert':
            for item in stack:
                if isinstance(item, (list, str)):
                    stack.push(item['qwert'.index(char)])
                    break
        elif char in 'yuiop':
            for item in stack:
                if isinstance(item, (list, str)):
                    stack.push(item[-' poiuy'.index(char)])
                    break
        elif char == 'n':
            stack.push(int(input()))
        elif char == 'N':
            stack.push(list(map(int, input().split())))
        elif char == 'c':
            stack.push(input())
        elif char == 'C':
            stack.push(input().split())
        elif char == '{':
            string = ''
            index += 1
            try:
                while code[index] != '}':
                    string += code[index]
                    index += 1
            except:
                pass
            for item in stack:
                if isinstance(item, (list, str)):
                    for i in item:
                        stack = run(string, [i] + stack)
        elif char == 'O':
            print(stack[0])
        elif char == 'B':
            for i, item1 in enumerate(stack):
                if isinstance(item1, int):
                    base = item1
                    break
            for item2 in stack[i+1:]:
                if isinstance(item2, int):
                    num = item2
                    break
            if base <= 64:
                alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
                stack.push(''.join(map(alphabet.__getitem__, numberToBase(num, base))))
        elif char == 'b':
            for item1 in stack:
                if isinstance(item1, str):
                    base = item1
                    break
            for item2 in stack:
                if isinstance(item2, int):
                    num = item2
                    break
            stack.push(''.join(map(base.__getitem__, numberToBase(num, len(base)))))
        elif char == 'D':
            for item1 in stack:
                if isinstance(item1, int):
                    base = item1
                    break
            for item2 in stack:
                if isinstance(item2, str):
                    num = item2
                    break
            stack.push(int(num, base))
        elif char == 'J':
            for item0 in stack:
                if isinstance(item0, int):
                    num = item0
                    break
            for i, item1 in enumerate(stack):
                if isinstance(item1, str):
                    fillchar = item1
                    break
            for item2 in stack[i+1:]:
                if isinstance(item2, str):
                    fillstr = item2
                    break
            stack.push(fillstr.rjust(num, fillchar))
        index += 1
    return stack
