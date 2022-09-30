'''
LIS - Longest increasing subsequence 최장 증가 부분 수열
LCS - Longest Common Subsequnce 최장 공통 부분 수열

'''
# 엑셀 LCS(Longest Common String) 최장공통부분문자열
str1 = input()  # BABJYP
str2 = input()  # ABCBJY

dp = [[0] * (len(str1)+1) for _ in range(len(str1)+1)]

for i in range(len(str1)):
    for j in range(len(str1)):
        if str2[i]==str1[j]:
            dp[i+1][j+1] = dp[i][j]+1

for g in dp:
    print(*g)
# ===========================================================

# 엑셀 LCS(Longest Common Subsequence) 최장공통부분수열  BABJYP  
str1 = input()  # BABJYP
str2 = input()  # ABPABY
dp = [[0] * (len(str1)+1) for _ in range(len(str1)+1)]

for i in range(len(str1)):
    for j in range(len(str1)):
        if str2[i]==str1[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else: dp[i+1][j+1] += max(dp[i+1][j],dp[i][j+1])
        
for g in dp:
    print(*g)
#====================================================================

# 엑셀 LIS(Longest Increasing Subsequence) 최장공통 부분수열   10 20 10 30 20 50
lst = list(map(int,input().split()))
dp = [1] * len(lst)
for i in range(len(lst)):
    for j in range(i):
        if lst[i]>lst[j]: dp[i] = max(dp[j]+1,dp[i])    # 만약 배열의 앞 원소가 작으면 그 작은 원소(0~i+1)의 dp값 +1 한 값과 큰 원소(i)의 dp 값 비교해서 삽입

print(dp)





















