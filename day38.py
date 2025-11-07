
def Prime_List(arr):
    pl=[]
    for n in arr:
        is_prime=True
        if n<2:
            is_prime=False   
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            pl.append(n)
    print(pl)
Prime_List([10,11,12,13,14,15,16,17])
Prime_List([22,25,27,45,23,12])
Prime_List([1,2,3,4,5,6])
Prime_List([6,12,18,24,66,42,10])
Prime_List([])








