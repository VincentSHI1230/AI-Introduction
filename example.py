import eightpuzzle as ep


BEGIN = ep.Box([2, 8, 3, 1, 6, 4, 7, 0, 5])
END = ep.Box([1, 2, 3, 8, 0, 4, 7, 6, 5])
front = [BEGIN]


def key(box: 'ep.Box') -> int:
    # 广度优先搜索
    # return len(Box.history)
    # 启发式搜索
    fr = box.value
    to = END.value
    fn = 0
    for i in range(9):
        a, b = fr.index(i), to.index(i)
        # 启发一
        # if a != b:
        #     fn += 1
        # 启发二
        fn += abs(a // 3 - b // 3) + abs(a % 3 - b % 3)
        # 启发三 (缺陷)
        # if a != b and fr[b] == to[a]:
        #     fn += 1
        # 启发四
        # if a != b:
        #     fn += 1
        #     if fr[b] == to[a]:
        #         fn += 1
    return fn


while front:
    front.sort(key=key)
    now = front.pop(0)
    print(now.history)
    if now.value == END.value:
        print(now)
        break
    front += now.expand()
