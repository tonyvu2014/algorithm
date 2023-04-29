# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# 2 = 1+1 = 2
# 3 = 1+1+1 = 2 +1 = 1 + 2 
# 4 = 1+1+1+1 = 2+1+1 = 1+ 2 +1 = 1+1 +2 = 2 + 2  
def stair_climb_way_counter(n):
    stair_climb_counter = [0] * (n+1)
    stair_climb_counter[0] = 1
    stair_climb_counter[1] = 1
    for i in range(2, n+1):
	    stair_climb_counter[i] = stair_climb_counter[i-1] + stair_climb_counter[i-2]

    return stair_climb_counter[n]

if __name__ == '__main__':
	print(str(stair_climb_way_counter(4)))
