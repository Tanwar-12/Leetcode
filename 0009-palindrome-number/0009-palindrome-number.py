from math import modf

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        x_str = str(x)
        x_list = []
        cont = 0
        for i, c in enumerate(x_str):
            x_list.append(c)

        if len(x_list) == 1:
            return True
        elif len(x_list) == 2:
            if x_list[0]==x_list[1]:
                return True
            else:
                return False
        elif len(x_list) == 3:
            if x_list[0]==x_list[2]:
                return True
            else:
                return False
        else:
            a = trunc(len(x_list) / 2)
            for j in range(0, a):
                k = len(x_list) - 1 - j
                if x_list[j] != x_list[k]:
                    return False
            return True
