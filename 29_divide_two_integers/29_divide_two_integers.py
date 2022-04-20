class Solution(object):

    def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        _dividend = abs(dividend)
        _divisor = abs(divisor)
        lookUp = [[1, _divisor]]
        idx = 0
        quotient = 0

        if _divisor == 1:
            quotient = _dividend
        else:
            while idx > -1:
                cnt = lookUp[idx][0]
                val = lookUp[idx][1]
                if val < _dividend:
                    if len(lookUp) <= idx+1:
                        lookUp.append([cnt + cnt, val + val])
                    _dividend -= val
                    quotient += cnt
                    idx += 1
                elif val == _dividend:
                    _dividend -= val
                    quotient += cnt
                    break
                else:
                    if idx > 0:
                        idx -= 1
                    else:
                        break

        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return quotient-1 if quotient >= 2147483648 else quotient
        else:
            return -abs(quotient)

    divide(2147, 2)
