class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def countLive(i,j):
            count=0
            directions=[[0,1],[1,0],[-1,0],[0,-1],[1,-1],[-1,1],[1,1],[-1,-1]]
            for dirs in directions:
                r=i+dirs[0]
                c=j+dirs[1]
                if r>=0 and r<len(board) and c>=0 and c<len(board[0]) and (board[r][c]==1 or board[r][c]==-1):
                    count+=1
            return count
        for i in range(len(board)):
            for j in range(len(board[0])):
                count=countLive(i,j)
                if board[i][j]==0:
                    if count==3:
                        board[i][j]=2
                elif board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j]=-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
                                                                           
                                                                           
                    
        
        
        
        
        
        