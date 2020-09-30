/* Problem Statement: Numbers of length N and value less than K
Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
NOTE: All numbers can only have digits from the given set. 

Approach: Let us try to solve for all the possible cases.
Let d be size of A.

Case 1: If B is greater than length of C or d is 0 then no such number is possible.

Case 2: If B is smaller than length of C then all the possible combination of digits of length B are valid.

Generate all such B digit numbers.
For the first position we can’t have 0 and for ther rest of (B - 1) position we can have all d possible digits.
Hence, Answer = d B if A contains 0 else (d-1) * ( d )(B-1)

Case 3: If B is equal to length of C
Construct digit array of C ( call it as digit[]).

Let First(i) be a number formed by taking first i digits of it.
Let lower[i] denote number of elements in A which are smaller than i.
It can be easily computed by idea similar to prefix sum.

For example:

First(2) of 423 is 42. 
If  A =  [ 0, 2] then lower[0] = 0, lower[0] = 0, lower[1]  = 1,  lower[2] = 1, lower[3] = 2  
Generate B digit numbers by dynamic programming. Let say dp[i] denotes the total numbers of length i which are less than first i digits of C.

Elements in dp[i] can be generated by two cases :

i) For all the Numbers whose First(i - 1) is less than First (i-1) of C, we can put any digit at i’th index.
Hence, dp[i] += (dp[i-1] * d)

ii) For all the Numbers whose First (i - 1) is same as First (i - 1) of C, we can only put those digits which are smaller than digit[i] .

Hence , dp[i] += lower[digit[i]]

Final answer will be dp[B]

Remark:
For first index don’t include 0 if B is not 1 and dp[0] will be 0.

Time Complexity = O(B)
*/





class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def get_count(self, A, B, base, index):
        if index >= len(base) or B==0:
            return 1
        current_max = int(base[index])
        rt = 0
        for x in A:
            if index == 0 and x ==0 and B!=1:
                continue
            if x > current_max:
                continue
            if x == current_max:
                if index >= len(base) -1:
                    continue
                rt = rt + self.get_count(A, B-1, base, index+1)
            else:
                rt = rt + len(A)**(B-1)
        return rt
                
    
    def solve(self, A, B, C):
        base = str(C)
        if len(base) < B:
            return 0
        
        index = 0
        if len(base) == B:
            return self.get_count(A, B, base, 0)
        rt = 0
        for x in A:
            if x == 0 and B!=1:
                continue
            if x==0 and x < C:
                rt +=1
            else:
                rt = rt + len(A)**(B-1)
        return rt
            
        
