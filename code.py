import matplotlib.pyplot as plt
import time
import math

# Initialize variables and lists
alu_update = [-1]
alu_update1 = [-1]
ac_value = 0
lis_tspex = [0]
lis_value = []
lis_dtspex = []
lis_shaz = [0]

# Ensure x and y have the same length by padding with None
def pad_list(data, target_len):
    return data + [None] * (target_len - len(data))

# Perform ALU operations and append results to lis_value
def instruction_value(op, rs, rt):
    global lis_value
    global ac_value

    if op.lower() == "add":
        ac_value = rs + rt
    elif op.lower() == "sub":
        ac_value = rs - rt
    elif op.lower() == "mul":
        ac_value = rs * rt
    elif op.lower() == "div":
        ac_value = rs / rt
    else:
        print("Unsupported operation.")
        return

    lis_value.append(ac_value)
    ac_value = 0

# Detect structural hazards and update ALU operations
def struct_hazard():
    global lis_tspex
    global lis_dtspex
    global lis_shaz
    global alu_update
    global alu_update1

    for x in range(len(lis_tspex) - 1):
        lis_dtspex.append(lis_tspex[x + 1] - lis_tspex[x])

    for x in range(len(lis_dtspex) - 1):
        if lis_dtspex[x + 1] <= 3:
            lis_shaz.append(1)
        if lis_dtspex[x + 1] < 3:
            for i in range(int(lis_dtspex[x])):
                alu_update.append(1)
                alu_update1.append(-1)
            for i in range(math.ceil(3 - lis_dtspex[x])):
                alu_update.append(0)
                alu_update1.append(1)
            try:
                if lis_dtspex[x + 2] < 3:
                    for i in range(int(lis_dtspex[x + 1])):
                        alu_update1.append(0)
                        alu_update.append(-1)
                    for i in range(math.ceil(3 - lis_dtspex[x + 1])):
                        alu_update1.append(-1)
                        alu_update.append(1)
            except IndexError:
                pass
        else:
            lis_shaz.append(0)
            for i in range(int(lis_dtspex[x])):
                alu_update.append(1)
                alu_update1.append(-1)
            alu_update.append(-1)
            alu_update1.append(-1)

# Printing the results
def printing():
    global lis_tspex
    global lis_dtspex
    global lis_shaz
    global lis_value
    global alu_update
    global alu_update1

    print("The values of accumulator:")
    for x in lis_value:
        print(x)
    
    print("Time Specification (tspex):")
    for x in lis_tspex:
        print(x)

    print("Differences in Time Specification (dtspex):")
    for x in lis_dtspex:
        print(x)

    print("Structural Hazards Detected (shaz):")
    for z in lis_shaz:
        print(z)

    print("ALU Update:")
    for x in alu_update:
        print(x)

    print("Other ALU Update:")
    for x in alu_update1:
        print(x)

# Plotting the graphs
def plot_graphs():
    global lis_tspex
    global lis_shaz
    global alu_update
    global alu_update1

    max_len = max(len(lis_tspex), len(alu_update), len(alu_update1))
    
    # Pad the lists to the same length
    lis_tspex = pad_list(lis_tspex, max_len)
    alu_update = pad_list(alu_update, max_len)
    alu_update1 = pad_list(alu_update1, max_len)
    lis_shaz = pad_list(lis_shaz, max_len)

    plt.figure(figsize=(12, 6))

    # Plot the first graph
    plt.subplot(2, 1, 1)
    plt.plot(lis_tspex, alu_update, label="ALU Update", marker='o')
    plt.plot(lis_tspex, alu_update1, label="ALU1 Update", marker='x')
    plt.plot(lis_tspex, lis_shaz, label="Structural Hazard", marker='s')
    plt.xlim(0, 25)
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("ALU and Structural Hazard Updates")
    plt.legend()

    # Plot the second graph (same data as the first)
    plt.subplot(2, 1, 2)
    plt.plot(lis_tspex, alu_update, label="ALU Update", marker='o')
    plt.plot(lis_tspex, alu_update1, label="ALU1 Update", marker='x')
    plt.plot(lis_tspex, lis_shaz, label="Structural Hazard", marker='s')
    plt.xlim(0, 25)
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Repeated ALU and Structural Hazard Updates")
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main function to run the program
def main():
    global lis_tspex
    current_time = time.time()

    while True:
        user_input = input("Instruction: ").strip()

        if user_input.lower() == 'done':
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid instruction format. Use: OPERATION RS RT")
            continue

        op, rs, rt = parts

        try:
            rs = int(rs)
            rt = int(rt)
        except ValueError:
            print("Register numbers must be integers.")
            continue

        if op not in ["ADD", "SUB", "MUL", "DIV"]:
            print("Unsupported operation. Use ADD, SUB, MUL, or DIV.")
            continue

        lis_tspex.append(round(time.time() - current_time, 2))
        instruction_value(op, rs, rt)
        struct_hazard()
        printing()

    plot_graphs()

# Start the program
if _name_ == "_main_":
    main()
