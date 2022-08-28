# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
records = {}
for i in range(n):
    s = list(input().split())
    name, ph = s[0], s[1]
    records[name] = ph
queries = []
try:
    while True:
        inp = input()
        if inp != '':
            queries.append(inp)
        else:
            break
except EOFError:
    pass

total = len(queries)
for i in queries:
    if i in records:
        print("{}={}".format(i, records[i]))
    else:
        print("Not found")
