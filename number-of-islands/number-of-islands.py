class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            for dirs in directions:
                r=i+dirs[0]
                c=j+dirs[1]
                if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]=="1":
                    grid[r][c]="#"
                    dfs(r,c)
        count=0
        directions=((0,1),(1,0),(-1,0),(0,-1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    grid[i][j]="#"
                    dfs(i,j)
                    count+=1
​
        return count
                    
                    
        
