def decodeString(s):
    stack = []
    string, curnum = "", 0
    for i in s:
        if i.isdigit():
            curnum = curnum * 10 + int(i)
        elif i == "[":
            stack.append(string)
            stack.append(curnum)
            string, curnum = "", 0
        elif i == "]":
            print(stack)
            num = stack.pop()
            prev = stack.pop()
            string = prev + num * string
        else:
            string += i
    return string

print(decodeString("3[a]2[bc]"))
"3[a]2[bc]"