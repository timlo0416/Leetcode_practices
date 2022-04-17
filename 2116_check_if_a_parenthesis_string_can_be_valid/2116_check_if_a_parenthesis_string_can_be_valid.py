class Solution(object):
    s = "())()))()(()(((())(()()))))((((()())(())"
    locked = "1011101100010001001011000000110010100101"
    # test case 1
    # "((()(()()))()((()()))))()((()(()"
    # "10111100100101001110100010001001"
    # test case 2
    # "())()))()(()(((())(()()))))((((()())(())"
    # "1011101100010001001011000000110010100101"
    # test case 3
    # "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
    # "100011110110011011010111100111011101111110000101001101001111"

    def canBeValid(s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """

        if len(s) % 2 != 0 or (s[0] == ")" and locked[0] == "1"):
            return False

        unlocked = 0
        left = 0
        right = 0
        for idx, i in enumerate(s):
            if locked[idx] == "0":
                unlocked += 1
            else:
                if i == ")":
                    if left:
                        left -= 1
                    elif unlocked:
                        unlocked -= 1
                    else:
                        return False
                else:
                    left += 1

        unlocked = 0
        locked = locked[::-1]
        s = s[::-1]
        for idx, i in enumerate(s):
            if locked[idx] == "0":
                unlocked += 1
            else:
                if i == "(":
                    if right:
                        right -= 1
                    elif unlocked:
                        unlocked -= 1
                    else:
                        return False
                else:
                    right += 1
        return True

    print(canBeValid(s, locked))
