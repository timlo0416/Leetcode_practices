class Solution(object):
    def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(S=[], left=0, right=0):
            # print("S = " + S)
            if len(S) == n * 2:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack()
        return ans


Solution.generateParenthesis(3)
