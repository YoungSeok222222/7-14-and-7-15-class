T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0 # testcase 바뀔 때마다 초기화
    for i in range(N): # 기준
        cnt = 0 # arr[i] 오른쪽 원소 중 더 작은 원소의 개수
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1
        # cnt 중 최대값
        if maxV < cnt:
            maxV = cnt
    print(f'#{tc} {maxV}')
######################################################
# TC = int(input())
# for T in range(1, TC+1): # testcase 마다
#     N = int(input()) # 가로의 길이
#     arr = list(map(int, input().split())) # 각 블럭의 높이
#     Max = 0 # 오른쪽에 비어 있는 블럭 개수가 가장 많은 경우 찾기
#     for i in range(N): # 각 블럭 마다
#         cnt = 0  # 기준 블럭 바뀔 때마다 리셋
#         for j in range(i+1, N): # 각 블럭의 오른쪽에 있는 비어 있는 블럭 개수 구하기
#             if arr[i] > arr[j]:
#                 cnt += 1
#         if cnt > Max:
#             Max = cnt
#     print(f'#{T} {Max}')