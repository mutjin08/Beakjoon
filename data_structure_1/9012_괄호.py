t = int(input())
brackets = []
for _ in range(t):
    brackets.append(input())

for bracket in brackets:
    cnt, vps = 0, 1
    for now in bracket:
        if now == ")":
            if cnt > 0:
                cnt -= 1
            else:
                vps = 0
                break
        else:
            cnt += 1
    if not vps or cnt>0:
        print("NO")
    else:
        print("YES")