# 18 factors is 1,2,3,6,9 total is 21   result is greater than 18 so it is abundant number


def is_Abundantnumber(n):
    divisor_sum = 0
    for   i in range(1,n):
        if n%i==0:
            divisor_sum+=i
    print("Abundant Number") if sum>n else print("not a abundant")
is_Abundantnumber(18)
is_Abundantnumber(26)
is_Abundantnumber(6)
is_Abundantnumber(9)
