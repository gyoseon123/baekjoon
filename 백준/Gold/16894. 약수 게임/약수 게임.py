def is_prime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

n = int(input())

if n == 1 or is_prime(n):
    print("koosaga")
    exit()

for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        if is_prime(n//i):
            print("cubelover")
        else:
            print("koosaga")
        break
        
