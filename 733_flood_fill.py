# https://leetcode.com/problems/flood-fill/

class Solution:
    def dfs(self, image: List[List[int]], sr: int, sc: int, original_color: int, color: int):
        
        if (sr < 0) or (sc < 0) or (sr >= len(image)) or (sc >= len(image[0])) or image[sr][sc] != original_color or image[sr][sc] == color:
            return
        else:
            image[sr][sc] = color
            self.dfs(image, sr - 1, sc, original_color, color)
            self.dfs(image, sr + 1, sc, original_color, color)
            self.dfs(image, sr, sc - 1, original_color, color)
            self.dfs(image, sr, sc + 1, original_color, color)
            
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        self.dfs(image, sr, sc, original_color, color)
            
        return image
