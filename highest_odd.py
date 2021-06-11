  
def highest_odd(li):
    odds = []
    for i in li:
        if i % 2 !=0:
            odds.append(i)
    return max(odds) 
print(highest_odd([11,2,3,12,10]))     