def golf(n):return iter(i for i in range(n+1,986899) if str(i)==str(i)[::-1] and all(i%j!=0 for j in range(2,i))).next()
