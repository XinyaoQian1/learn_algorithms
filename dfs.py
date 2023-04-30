"""
# @File    :    dfs.py
# @Time    :    17/01/2023 15:29
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: 
"""

directions = [(1,0),(0,-1),(0,1),(-1,0)]
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        count = 0

        # for every point
        for i in range(row):
            for j in range(column):
                # flood
                if grid[i][j] == "1":
                    grid[i][j]= '0'
                    self.dfs(grid,i,j)

                    count += 1

        return count

    def dfs(self,grid,i,j):
        queue = deque([(i,j)])
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                if grid[nx][ny] == '1' and 0<=nx<=len(grid) and 0<=ny<=len(grid[0]):
                    grid[nx][ny] = '0'
                    queue.append((nx,ny))


