def solve():
    t = int(input())
    H_kit = []
    A_kit = []
    cnt = [0] * 100001

    for _ in range(t):
        
        H, A = map(int, input().split())

        H_kit.append(H)
        A_kit.append(A)
        cnt[H] += 1

    for i in range(t):
        home_games = t - 1
        home_games += cnt[A_kit[i]]

        away_games = 2 * (t - 1) - home_games

        print(home_games, away_games)

if __name__ == "__main__":
    solve()
        


