from itertools import permutations 
from itertools import combinations 
  
comb = combinations([1, 2, 3], 2) 
  
# Print the obtained combinations 
for i in list(comb): 
    print(i) 

perm = permutations([1, 2, 3]) 

for i in list(perm): 
    print(i)
