class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookUpDict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                      "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                      "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                      "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        length = len(digits)
        pivot = 0
        ans = []

        def backTrack(idx, combination):
            if length == 0:
                return
            if idx == length:
                ans.append(combination)
                return
            for i in lookUpDict[digits[idx]]:
                new_combination = combination+i
                backTrack(idx+1, new_combination)

        backTrack(pivot, "")
        return(ans)
