from collections import deque


def reverseInParentheses(inputString):
    if len(inputString) <= 1:
        return inputString
    dq = deque()
    current = ""
    for s in inputString:
        if s == "(":
            dq.append(current)
            current = ""
        elif s == ")":
            current = current[::-1]
            if len(dq) > 0:
                last = dq.pop()
                last = last + current
                current = last
        else:
            current += s

    if len(dq) > 0:
        return dq.pop()
    else:
        return current


if __name__ == '__main__':
    print(reverseInParentheses("(abc)"))
    print(reverseInParentheses("foo(bar)baz"))
    print(reverseInParentheses("(())(((())))"))
    print(reverseInParentheses("foo(bar)baz(blim)"))
    print(reverseInParentheses("foo(bar(baz))blim"))
    print(reverseInParentheses("((bar))"))
    print(reverseInParentheses("abc(def)gh(ij(klm))"))
    print((reverseInParentheses("((stu((xyz)wv)))")))
    print(reverseInParentheses("abc((ghi((mno((stu((xyz)wv))rqp))lkj))fed)((abcd))"))

