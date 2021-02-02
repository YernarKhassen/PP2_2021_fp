class Solution(object):
    def subtractProductAndSum(self, n):
        pofd = 1
        sum = 0
        n = str(n)
        for i in n:
            pofd*=int(i)
            sum+=int(i)
        return(pofd - sum)

    