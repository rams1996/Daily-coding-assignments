class Solution {

    public void dfs(int i, int j, int[][] dirs, int n, int m, char[][] grid){
        for (int[] d:dirs){
            int r=i+d[0];
            int c=j+d[1];
            if (r>=0 && r<n && c>=0 && c<m && grid[r][c]=='1'){
                grid[r][c]='#';
                dfs(r,c,dirs,n,m,grid);
            }
            
        }
    }
    public int numIslands(char[][] grid) {
        int count=0;
        int[][] dirs = new int[][]{{1,0},{0,1},{0,-1},{-1,0}};
        int n=grid.length;
        int m=grid[0].length;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if (grid[i][j]=='1'){
                    grid[i][j]='#';
                    dfs(i,j,dirs,n,m,grid);
                    count++;
                    
            }
            }
        }
        return count;
        
        
    }
}