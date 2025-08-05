"""
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

===
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

===
#1 3
#2 0
#3 4
"""
T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    x = 0
    stop_count = 0

    while x + K < N:
        find = [num for num in station if x < num <= x + K]
        if find:
            c = max(find)
            x = c
            stop_count += 1
        else:
            stop_count = 0
            break

    print(f"#{test_case} {stop_count}")
# T = int(input())
#
# for t in range(1, T+1):
#     K, N, M = map(int, input().split()) # K : 한번충전으로 이동가능 정류장수
#     charge_stations = list(map(int,input().split()))# N: 종점 # M : 충전기가 설치된 정류장 수
#
#     pos = 0 # 현재 버스의 위치
#     cnt = 0 # 충전을 한 횟수
#     while pos + K < N:
#         for step in range(K, 0, -1): #최소 충전을 해야함으로 간격을 좁혀나간다
#             if (pos + step) in charge_stations:
#                 pos += step
#                 cnt += 1
#                 break  # 충전소 도달 다시 while문으로 가고 충전횟수+1
#         else:
#             cnt = 0  # 종점에 도착 할 수 없을 때
#             break
#
#     print(f"#{t} {cnt}")
