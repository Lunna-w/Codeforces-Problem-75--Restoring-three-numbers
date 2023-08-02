a,b,c,d=list(map(int, input() .split()))

list=[]

list.append(a)
list.append(b)
list.append(c)
list.append(d)




max_sum=max(list)
list.remove(max_sum)


true_a=max_sum-list[0]

true_b=max_sum-list[1]

true_c=max_sum-list[2]
print(true_a, true_b,true_c)

#print(true_a,true_b,true_c)

