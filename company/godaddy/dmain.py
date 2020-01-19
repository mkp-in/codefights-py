def domainType(domains):
    a = []
    for d in domains:
        t = d.split(".")[-1]
        print(t[-1])
        if t == "com":
            a.append("commercial")
        elif t == "org":
            a.append("organization")
        elif t == "net":
            a.append("network")
        else:
            a.append("information")
    return a


if __name__ == '__main__':
    print(domainType(["en.wiki.org",
 "codesignal.com",
 "happy.net",
 "code.info"]))