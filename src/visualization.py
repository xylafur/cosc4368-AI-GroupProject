def get_QTables(file):
    lines = file.read().splitlines()

    index = lines.index("Resulting Q Table") + 1
    lines = lines[index : ]
    index = 0
    tables = [[]]  

    while index < len(lines):
        cell = 0
        # permuation with replacement for 7 binary values = 128
        for table in range(128):
            tables[table].append(get_QTable(lines[index]))
            index += 1
        cell += 1


def get_QTable(line):
    table = {}
    values = []
    lines = line.split(" = ")

    location = line[1:5]
    location = '(' + location + ')'

    lines[1] = lines[1].strip("{}")
    valueLines = lines[1].split(',')
    
    str1 = ": "
    
    for i in range(4):
        values.append(valueLines[i][valueLines[i].find(str1) + 1 : ])

    table[location] = values

    return table



def main():
    ex_1 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment1", "r")
    #ex_2 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment2", "r")
    #ex_3 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment3", "r")
    #ex_4 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment4", "r")
    #ex_5 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment5", "r")

    ex_1_tables = get_QTables(ex_1)
    #ex_2_tables = get_QTables(ex_2)
    #ex_3_tables = get_QTables(ex_3)
    #ex_4_tables = get_QTables(ex_4)
    #ex_5_tables = get_QTables(ex_5)

    ex_1.close()
    #ex_2.close()
    #ex_3.close()
    #ex_4.close()
    #ex_5.close()


main()