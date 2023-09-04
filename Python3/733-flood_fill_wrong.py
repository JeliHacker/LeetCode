def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    def dfs(x, y):
        print("dfs()", x, y, image[x][y])
        if image[x][y] == old_color:
            if color != 2:
                print("color has changed!!! = ", color)
            image[x][y] = color
            print(f"image[{x}][{y}] now equals {color}")

            for direction in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                if 0 <= direction[0] < len(image) and 0 <= direction[1] < len(image[0]):
                    print("direction", direction)
                    dfs(direction[0], direction[1])
                else:
                    print("invalid coordinates", direction, "current x y = ", x, y)

    old_color = image[sr][sc]
    dfs(sr, sc)

    return image
    

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))