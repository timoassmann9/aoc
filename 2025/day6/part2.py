import math

def calc(problem: list[str]):
    problem = [p.strip() for p in problem]
    values = list(map(int, problem[:-1]))
    operator = problem[-1]

    if operator == "*":
        return math.prod(values)
    if operator == "+":
        return sum(values)

with open("input.txt") as f:
    data = f.read()

lines = data.split("\n")
lines = [line for line in lines if line]

l = len(lines[0])
solutions = list()
end = l
for i in reversed(range(l)):
    chars = [line[i] for line in lines]
    if all(char == chars[0] for char in chars) or i == 0:
        problem = list()
        for j in reversed(range(i if i == 0 else i + 1, end)):
            problem.append("".join([line[j] for line in lines if line[j]]))

        solutions.append(calc([line[start:i if i < l - 1 else i + 1] for line in lines]))
        start = i + 1

print(sum(solutions))