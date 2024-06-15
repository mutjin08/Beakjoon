n = int(input())

cmds = []
for _ in range(n):
    # process input
    cmds.append(input().split())

stack = []
for cmd in cmds:
    if len(cmd)>1:
        x = int(cmd[1])
    cmd = cmd[0]

    # command execution
    if cmd == "push":
        stack.append(x)
    elif cmd == "pop":
        if stack:
            print(stack.pop()) #error
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        print("error")