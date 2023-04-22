N, SejunX, SejunY, mineX, mineY = map(int, input().split())

tR = mineX - SejunX
tU = mineY - SejunY

def dd():
    global tR, tU, N
    if tR < 0 or tU < 0:
        print(-1)
        return

    if tR + tU <= N:
        ans = "R"*tR + "U"*tU + "R"*(N-tR-tU)
        print(ans)
        return

    m = (tR + tU) // N      #몫
    n = (tR + tU) % N       #나머지
    for bR in range(n, -1, -1):
        bU = n - bR
        r = (tR - bR)/m - bR
        u = (tU - bU)/m - bU
        # print(f'r={r} and u={u}')
        if r >= 0 and u >= 0 and r % 1 == 0 and u % 1 == 0:
            r = int(r)
            u = int(u)
            if bR + bU + r + u == N:
                print("R"*bR+"U"*bU+"R"*r+"U"*u)
                return
    else:
        print(-1)
        return

dd()
