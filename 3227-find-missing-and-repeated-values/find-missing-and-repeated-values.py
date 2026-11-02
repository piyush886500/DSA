class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        total=0
        for i in range(1,rows*cols+1):
            total+=i

        repeated = 0
        dict = {}
        arr_sum=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in dict:
                    repeated = grid[i][j]
                else:
                    dict[grid[i][j]] = 0
                arr_sum += grid[i][j]


        return [repeated,repeated+(total-arr_sum)]