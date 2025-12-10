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
        problem: list[str] = list()
        for j in reversed(range(i if i == 0 else i + 1, end)):
            problem.append("".join([line[j] for line in lines if line[j] != " "]))
        for x, number in enumerate(problem):
            if number.endswith("+") or number.endswith("*"):
                number, operator = number[:-1], number[-1]
                problem[x] = number
                problem.append(operator)
                break
        solutions.append(calc(problem))
        end = i

print(sum(solutions))