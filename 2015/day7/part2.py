MASK_16 = 0xFFFF

class Instruction:
    def __init__(self, in1, in2, out, gate) -> None:
        self.in1 = in1
        self.in2 = in2
        self.out = out
        self.gate = gate
        self.in_count = sum(1 for x in (self.in1, self.in2) if x)
        self.processed = False

    def __str__(self) -> str:
        return f"In1: {self.in1}, In2: {self.in2}, Out: {self.out}, Gate: {self.gate}, Processed: {self.processed}"
    
    def __repr__(self) -> str:
        return f"In1: {self.in1}, In2: {self.in2}, Out: {self.out}, Gate: {self.gate}, Processed: {self.processed}"

def mask(x):
    return x & MASK_16

def AND(x, y):
    return mask(x & y)

def OR(x, y):
    return mask(x | y)

def NOT(x):
    return mask(~x)

def RSHIFT(x, n):
    if n > 0:
        return mask(x >> n)
    
def LSHIFT(x, n):
    if n > 0:
        return mask(x << n)
    
def process(instruction: Instruction):
    global wires

    v1 = instruction.in1
    v2 = instruction.in2
    values = [v1, v2]
    for i, value in enumerate(values):
        if not value:
            continue

        if isinstance(value, str):
            try:
                values[i] = wires[value]
            except KeyError:
                return
            
    v1, v2 = values

    match instruction.gate:
        case "NOT":
            wires[instruction.out] = NOT(v1)
        case "AND":
            wires[instruction.out] = AND(v1, v2)
        case "OR":
            wires[instruction.out] = OR(v1, v2)
        case "RSHIFT":
            wires[instruction.out] = RSHIFT(v1, v2)
        case "LSHIFT":
            wires[instruction.out] = LSHIFT(v1, v2)
        case "ASSIGN":
            wires[instruction.out] = v1
        case _:
            return

    instruction.processed = True

with open("input2.txt") as f:
    data = f.read()

data = data.split("\n")

instructions: list[Instruction] = list()
for line in data:
    sep = line.index("->")
    out = line[sep+3:]
    ins = line[:sep-1]
    if ins.startswith("NOT"):
        gate = ins[:3]
        in1 = ins[4:]
        in2 = None

        in1 = int(in1) if in1.isnumeric() else in1
    elif " " not in ins:
        in1 = int(ins) if ins.isnumeric() else ins
        in2 = None
        gate = "ASSIGN"
    else:
        space1 = ins.index(" ")
        space2 = ins.index(" ", space1+1)

        in1 = ins[:space1]
        in2 = ins[space2+1:]
        gate = ins[space1+1:space2]

        in1 = int(in1) if in1.isnumeric() else in1
        in2 = int(in2) if in2.isnumeric() else in2

    instruction = Instruction(in1, in2, out, gate)
    instructions.append(instruction)

wires = dict()

while not all(instruction.processed for instruction in instructions):
    not_processed = [instruction for instruction in instructions if not instruction.processed]
    for instruction in not_processed:
        process(instruction)

for k, v in wires.items():
    print(k, v)

# diesen Teil nochmal im Programm machen, ohne den Input umzuschreiben:
# Lösung von Teil1 an b, alle wires reset