class Solution:
    def helper(self,image:List[List[int]],sr:int,sc:int ,target:int,color) -> List[List[int]]: 
        image[sr][sc] = color
        if sr-1 >= 0 and image[sr-1][sc] == target:
            self.helper(image,sr - 1, sc,target,color)
        if sr+1 < len(image) and image[sr+1][sc] == target:
            self.helper(image,sr + 1, sc,target,color)
        if sc-1 >= 0 and image[sr][sc-1] == target :
            self.helper(image,sr, sc - 1,target,color)
        if sc+1 < len(image[0]) and image[sr][sc+1] == target:
            self.helper(image,sr, sc + 1,target,color)
        return image
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            return self.helper(image,sr,sc,image[sr][sc],color)
        return image