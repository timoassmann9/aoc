with open("input.txt", "r") as f:
    data = f.read()

dimensions_list = data.split()
total_ribbon = 0
for dimensions in dimensions_list:
    length, width, height = tuple(map(int, dimensions.split("x")))
    dims = [length, width, height]
    dims.remove(max(dims))
    side1, side2 = tuple(dims)
    perimeter = 2 * (side1 + side2)
    bow = length * width * height
    ribbon = perimeter + bow
    total_ribbon += ribbon
print(total_ribbon)