def define_corners(x1,y1,x2,y2):
    if x2 <= x1 or y2>=y1:
        return False
    coords = []
    coords.append([x1,y1])
    coords.append([x2,y1])
    coords.append([x1,y2])
    coords.append([x2,y2])
    return coords

def compare_sides(rectangles):
    r1 = rectangles[0]
    r2 = rectangles[1]
    intercecting = True
    if r2[1][0] <= r1[0][0]:
        intercecting = False
    if r2[0][0] >= r1[1][0]:
        intercecting = False
    if r2[2][1] >= r1[0][1]:
        intercecting = False
    if r2[0][1] <= r1[3][1]:
        intercecting = False
    return intercecting
    

while __name__ == "__main__":
    rectangles = []
    for x in range(2):
        print(f"Info for rectangle {x+1}")
        x1 = int(input("Enter X coordinate 1 (top left)"))
        y1 = int(input("Enter Y coordinate 1 (top left)"))
        x2 = int(input("Enter X coordinate 2 (bottom right)"))
        y2 = int(input("Enter Y coordinate 2 (bottom right)"))
        rectangles.append(define_corners(x1,y1,x2,y2))

    print(compare_sides(rectangles))