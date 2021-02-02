class Solution(object):
    def largestAltitude(self, gain):
        mass = []
        x = 0
        mass += [x]
        for i in gain:
            mass += [x + i]
            x = x + i
        max = -999
        for i in mass:
            if i > max:
                max = i
        return max

