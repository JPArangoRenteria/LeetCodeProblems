class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        acc = triangle[0][0]
        indexes = 0
        for i in range(1,len(triangle)):
            poss_sums = []
            for j in range(0,len(triangle[i])):
                if j == indexes or j == indexes +1:
                    poss_sums.append(triangle[i][j])
                    if j == indexes:
                        indexes = j
                    if j == indexes+1:
                        indexes = j-1
                elif i == len(triangle)-1:
                    poss_sums.append(triangle[i][j])
                print(poss_sums)
            acc = min(poss_sums) + acc
            print(acc)
        return acc
