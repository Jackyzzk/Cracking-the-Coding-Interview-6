class Solution(object):
    """
编写函数，实现许多图片编辑软件都支持的「颜色填充」功能。
待填充的图像用二维数组 image 表示，元素为初始颜色值。
初始坐标点的横坐标为 sr 纵坐标为 sc。需要填充的新颜色为 newColor 。
「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。
请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。

输入：
image =
[[1,1,1],
 [1,1,0],
 [1,0,1]]
sr = 1, sc = 1, newColor = 2
输出：
[[2,2,2],
 [2,2,0],
 [2,0,1]]
解释:
初始坐标点位于图像的正中间，坐标 (sr,sc)=(1,1) 。
初始坐标点周围区域上所有符合条件的像素点的颜色都被更改成 2 。
注意，右下角的像素没有更改为 2 ，因为它不属于初始坐标点的周围区域。

image 和 image[0] 的长度均在范围 [1, 50] 内。
初始坐标点 (sr,sc) 满足 0 <= sr < image.length 和 0 <= sc < image[0].length 。
image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535] 内。
链接：https://leetcode-cn.com/problems/color-fill-lcci
    """
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(x, y):
            que = [(x, y)]
            image[x][y] = newColor
            visited[x][y] = 1
            while que:
                x, y = que.pop()
                for a, b in direction:
                    if 0 <= x + a < row and 0 <= y + b < column:
                        if image[x + a][y + b] == self.old and not visited[x + a][y + b]:
                            que.append((x + a, y + b))
                            image[x + a][y + b] = newColor
                            visited[x + a][y + b] = 1

        self.old = image[sr][sc]
        row, column = len(image), len(image[0])
        visited = [[0] * column for i in range(row)]
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dfs(sr, sc)
        return image


def main():
    # image = [[1,1,1],
    #          [1,1,0],
    #          [1,0,1]]
    # sr, sc, newColor = 1, 1, 2
    image = [[0,0,0],
             [0,1,1]]
    sr, sc, newColor = 1, 1, 1
    test = Solution()
    ret = test.floodFill(image, sr, sc, newColor)
    print(ret)


if __name__ == '__main__':
    main()
