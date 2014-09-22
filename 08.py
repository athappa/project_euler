#Project Euler #8

'''
The four adjacent digits in the 100 digit number that have the greatest
product are 9x9x8x9 = 5832.

Find the 13 adjacent digits in the 1000 digit number that have the 
greatest product
'''
import time
start = time.time()

n = '\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

#Import Modules
import operator
from operator import mul

#Put all of the 
def greatest_product():
	global list
	list = []
	for i in n:
		list.append(int(i))
	return list

greatest_product()

def lists():
	global seq_13
	seq_13 = []
	
	
	count = 0
	for i in list:
		x = list[count:count+13]
		if len(x) == 13:
			seq_13.append(x)
			count += 1
	return seq_13
print lists()

num_list_fin = []
for num_item in seq_13:
	num_item_u = [reduce(lambda x,y: x*y, num_item)]
	num_item_u.append(num_item)
	num_list_fin.append(num_item_u)


num_list_fin.sort(key=lambda x: int(x[0]))
print num_list_fin[len(num_list_fin)-1]

elapsed = (time.time() - start)
print "time: %s seconds" % elapsed
#[23514624000, [5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5]]


