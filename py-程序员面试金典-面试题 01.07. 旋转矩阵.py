class Solution(object):
    """
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。
请你设计一种算法，将图像旋转 90 度。不占用额外内存空间能否做到？
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 主对角线翻转，再垂直翻转
        row, column = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(i + 1, column):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(row):
            for j in range(1 + column >> 1):
                matrix[i][j], matrix[i][column - 1 - j] = matrix[i][column - 1 - j], matrix[i][j]
        return matrix


def main():
    matrix = \
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = \
    [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    test = Solution()
    ret = test.rotate(matrix)
    for x in ret:
        print(x)


if __name__ == '__main__':
    main()
