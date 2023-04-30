"""
# @File    :    circular_index.py
# @Time    :    14/02/2023 17:04
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: 
"""
def countMax( l):
    right = left = 0
    cnt = max_count = 1
    pre = l[0]

    while right < len(l):
        r = l[right]

        if r == pre:
            cnt += 1
            max_count = max(max_count, cnt)
        else:
            cnt = 1
        pre = r
        right += 1

    return max_count

s = [1,1,-1, 1,0,0,0]
print(countMax(s))