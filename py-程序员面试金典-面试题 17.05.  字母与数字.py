class Solution(object):
    """
给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。
返回该子数组，若存在多个最长子数组，返回左端点最小的。若不存在这样的数组，返回一个空数组。
输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
输入: ["A","A"]
输出: []
array.length <= 100000
链接：https://leetcode-cn.com/problems/find-longest-subarray-lcci
    """
    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """
        acc, rec1, rec2 = 0, {0: -1}, {}
        begin, end, length = 0, 0, 0

        for i, x in enumerate(array):
            if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
                acc += 1
            else:
                acc -= 1
            if acc not in rec1:
                rec1[acc] = i
            else:
                rec2[acc] = i
                if i - rec1[acc] + 1 > length:
                    begin, end, length = rec1[acc] + 1, i + 1, i - rec1[acc] + 1  # 左开右闭

        if not acc:
            return array
        if not end:
            return []
        return array[begin:end]


def main():
    array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    array = ["A","A"]
    array = ["A","1"]
    array = ["A","B","B","2","3"]
    array = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y",
             "z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I",
             "V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10",
             "93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44",
             "R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84",
             "44","96","96","y","M"]
    # ["52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X",
    # "33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81",
    # "T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5"]
    test = Solution()
    ret = test.findLongestSubarray(array)
    print(ret)


if __name__ == '__main__':
    main()
