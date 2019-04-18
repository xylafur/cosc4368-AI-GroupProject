import csv
import os

VISUALS_DIRECTORY = "Visuals"
ACTIONS = ['Position', 'N', 'S', 'E', 'W']

def get_QTables(file, outputFileName):
    lines = file.read().splitlines()

    index = lines.index("Resulting Q Table") + 1
    lines = lines[index : ]
    index = 0
    lineCount = 0
    stateSpace = ""
    tables = {}  
    tableEntries = []

    for line in lines:
        if line.strip():
            if "(0, 0" in line:
                if lineCount > 0:
                    tables[stateSpace] = tableEntries
                    tableEntries = []
                    stateSpace = ""

                lineCount = 0
                stateSpace = line[7: line.index(") =")]

            tableEntries.append(get_QTable(line))
            lineCount +=1    

    if not os.path.isdir(VISUALS_DIRECTORY):
        os.mkdir(VISUALS_DIRECTORY)

    orgdir = os.getcwd()
    os.chdir(VISUALS_DIRECTORY)

    with open(outputFileName, "w", newline='') as file:
        writer = csv.writer(file, delimiter=',')

        for key, value in tables.items():
            writer.writerow([key])
            writer.writerow([a for a in ACTIONS])

            for values in value:
                for k, vals in values.items():                   
                    [float(i) for i in vals]                    
                    writer.writerow([k] + vals)
                

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
    ex_2 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment2", "r")
    ex_3 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment3", "r")
    ex_4 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment4", "r")
    ex_5 = open("C:\\Users\\Bobby\\source\\repos\\AI\\GroupProject\\src\\ExperimentOutput\\Experiment5", "r")

    ex_1_tables = get_QTables(ex_1, "Experiment1.csv")
    ex_2_tables = get_QTables(ex_2, "Experiment2.csv")
    ex_3_tables = get_QTables(ex_3, "Experiment3.csv")
    ex_4_tables = get_QTables(ex_4, "Experiment4.csv")
    ex_5_tables = get_QTables(ex_5, "Experiment5.csv")

    ex_1.close()
    ex_2.close()
    ex_3.close()
    ex_4.close()
    ex_5.close()


main()