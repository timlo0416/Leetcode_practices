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

        unlocked_brace_cnt = 0
        locked_open_brace_cnt = 0
        locked_close_brace_cnt = 0
        locked_diff = 0
        for idx, i in enumerate(s):
            if locked[idx] == "1":
                if i == "(":
                    locked_diff += 1
                else:
                    locked_diff -= 1
        print("locked_diff = " + str(locked_diff))

        temp_locked_diff = locked_diff
        for idx, i in enumerate(s):
            if locked[idx] == "0":
                unlocked_brace_cnt += 1
                if temp_locked_diff > 0 and locked_open_brace_cnt > 0:
                    unlocked_brace_cnt -= 1
                    locked_open_brace_cnt -= 1
                    temp_locked_diff -= 1
            else:
                if i == "(":
                    locked_open_brace_cnt += 1
                else:
                    locked_close_brace_cnt += 1
                    if locked_open_brace_cnt > 0:
                        locked_open_brace_cnt -= 1
                        locked_close_brace_cnt -= 1
                    elif unlocked_brace_cnt > 0:
                        unlocked_brace_cnt -= 1
                        locked_close_brace_cnt -= 1
                    elif temp_locked_diff < locked_diff:
                        temp_locked_diff += 1
                        unlocked_brace_cnt += 1
                        locked_close_brace_cnt -= 1
                    else:
                        return False
            print("[STEP " + str(idx) + "]")
            print("unlocked_brace_cnt = " + str(unlocked_brace_cnt))
            print("locked_open_brace_cnt = " + str(locked_open_brace_cnt))
            print("locked_close_brace_cnt = " + str(locked_close_brace_cnt))
            print("temp_locked_diff = " + str(temp_locked_diff))

        if locked_open_brace_cnt != 0:
            return False
        if locked_close_brace_cnt != 0:
            return False
        if unlocked_brace_cnt % 2 != 0:
            return False
        return True

    print(canBeValid(s, locked))
