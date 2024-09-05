n = int(input())
num = [11,9,9,9,8,8,8,8,8,8]
solved = ["ABCDEFGHJLM", "ACEFGHILM", "ACEFGHILM", "ABCEFGHLM", "ACEFGHLM", "ACEFGHLM", "ACEFGHLM", "ACEFGHLM", "ACEFGHLM", "ABCFGHLM"]
print(num[n-1]) 
print(" ".join(solved[n-1]))