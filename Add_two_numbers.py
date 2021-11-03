def split(a):
	return [char for char in a]
def addTwoNumbers(l1,l2):
	l1_rev=[]
	l2_rev=[]
	s1=""
	s2=""
	s1_int=0
	s2_int=0
	sum_l1=0
	sum_l2=0
	sum1=""
	sum1_int=0
	final_1=[]
	final_2=[]

	for i in range(len(l1)-1,-1,-1):
		l1_rev.append(l1[i])

	for i in range(len(l2)-1,-1,-1):
		l2_rev.append(l2[i])
	
	for i in l1_rev:
		s1+=str(i)
	s1_int=int(s1)
	print(s1_int)

	for i in l2_rev:
		s2+=str(i)
		s2_int=int(s2)
	print(s2_int)

	sum1_int=s1_int+s2_int

	sum1=str(sum1_int)
	print(sum1)

	rev=0
	r=0

	while(sum1_int!=0):
		r=sum1_int%10
		rev=rev*10+r
		sum1_int=sum1_int//10
	rev_str=str(rev)
	final_1=split(rev_str)
	print(final_1)

	for i in final_1:
		final_2.append(int(i))
	
	print(final_2)
	

		


addTwoNumbers([2,4,3],[5,6,4])
