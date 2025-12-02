with open("input.txt", "r") as f:
    data = f.read()

dimensions_list = data.split()
total_paper = 0
for dimensions in dimensions_list:
    length, width, height = tuple(map(int, dimensions.split("x")))
    side1 = length * width
    side2 = width * height
    side3 = height * length

    area = 2 * (side1 + side2 + side3)
    smallest_side = min(side1, side2, side3)

    paper = area + smallest_side
    total_paper += paper

print(total_paper)