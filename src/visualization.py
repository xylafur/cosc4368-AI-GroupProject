import csv
import os
import matplotlib.pyplot as plt
import numpy as np

VISUALS_DIRECTORY = "Visuals"
EXPERIMENT_DIRECTORY = "ExperimentOutput"
HEATMAP_DIRECTORY = "HeatMaps"
ACTIONS = ['Position', 'N', 'S', 'E', 'W']

def get_QTables(file, outputFileName):

    if not os.path.isdir(VISUALS_DIRECTORY):
            os.mkdir(VISUALS_DIRECTORY)

    orgdir = os.getcwd()
    os.chdir(VISUALS_DIRECTORY)

    lines = file.read().splitlines()

    create_heatMap(lines, file)

    index = lines.index("Resulting Q Table") + 1
    lines = lines[index : ]
    index = 0
    lineCount = 0
    stateSpace = ""
    tables = {}  
    tableEntries = []
    
    

    if "SmallStatespace" not in file.name:
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

        

        with open(outputFileName, "w", newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([file.name[ : file.name.index('.')]])

            for key, value in tables.items():
                writer.writerow([key])
                writer.writerow([a for a in ACTIONS])

                for values in value:
                    for k, vals in values.items():                   
                        [float(i) for i in vals]                    
                        writer.writerow([k] + vals)
    else:
        tables = {}
        state = "True"
        positionValues = []

        for line in lines:
            if line.strip():
                newState = line[7 : line.index(") =")]
                if newState != state: 
                    tables[state] = positionValues
                    state = newState
                    positionValues = []
                else:
                    positionValues.append(get_QTable(line))
        # Add any leftover data to table
        if positionValues:
            tables[state] = positionValues

        with open(outputFileName, "w", newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([file.name[ : file.name.index('.')]])

            for key, value in tables.items():
                writer.writerow([key])
                writer.writerow([a for a in ACTIONS])

                for values in value:
                    for k, vals in values.items():                   
                        [float(i) for i in vals]                    
                        writer.writerow([k] + vals)
                
    os.chdir(orgdir)
                

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

def create_heatMap(lines, file):
    index = lines.index("Heatmap of visited locations:") + 1
    index2 = lines.index("Movements over time for the agent: ")
    newLines = lines[index : index2 ]
    data = []
    validData = []
    temp = []
    baseFileName = newFileName = file.name[ : file.name.index('.')]

    rows = ['0','1','2','3','4']
    cols = rows

    for line in newLines:
        if line:
            data.append(line.strip().split(' '))
    for row in data:
        temp = [int(i) for i in row] 
        validData.append(temp)

    visited = np.array(validData)

    fig, ax = plt.subplots()

    ax.set_xticks(np.arange(len(rows)))
    ax.set_yticks(np.arange(len(cols)))

    ax.set_xticklabels(rows)
    ax.set_yticklabels(cols)

    for i in range(len(rows)):
        for j in range(len(cols)):
            text = ax.text(j, i, visited[i,j], ha="center", va="center")
    
    ax.set_title(baseFileName + ": Number of Visits per Cell")
    im = ax.imshow(visited)

    if not os.path.isdir(HEATMAP_DIRECTORY):
        os.mkdir(HEATMAP_DIRECTORY)

    orgdir = os.getcwd()
    os.chdir(HEATMAP_DIRECTORY)

    newFileName = baseFileName + '_HeatMap.png'
    plt.savefig(newFileName)

    os.chdir(orgdir)

def generate_csv():
    if not os.path.isdir(EXPERIMENT_DIRECTORY):
        os.mkdir(EXPERIMENT_DIRECTORY)

    orgdir = os.getcwd()
    os.chdir(EXPERIMENT_DIRECTORY)

    ex_1_1 = open("Experiment1_1.txt", "r")
    ex_2_1 = open("Experiment2_1.txt", "r")
    ex_3_1 = open("Experiment3_1.txt", "r")
    ex_4_1 = open("Experiment4_1.txt", "r")
    ex_5_1 = open("Experiment5_1.txt", "r")

    ex_1_1_tables = get_QTables(ex_1_1, "Experiment1_1.csv")
    ex_2_1_tables = get_QTables(ex_2_1, "Experiment2_1.csv")
    ex_3_1_tables = get_QTables(ex_3_1, "Experiment3_1.csv")
    ex_4_1_tables = get_QTables(ex_4_1, "Experiment4_1.csv")
    ex_5_1_tables = get_QTables(ex_5_1, "Experiment5_1.csv")

    ex_1_1.close()
    ex_2_1.close()
    ex_3_1.close()
    ex_4_1.close()
    ex_5_1.close()

    ex_1_2 = open("Experiment1_2.txt", "r")
    ex_2_2 = open("Experiment2_2.txt", "r")
    ex_3_2 = open("Experiment3_2.txt", "r")
    ex_4_2 = open("Experiment4_2.txt", "r")
    ex_5_2 = open("Experiment5_2.txt", "r")

    ex_1_2_tables = get_QTables(ex_1_2, "Experiment1_2.csv")
    ex_2_2_tables = get_QTables(ex_2_2, "Experiment2_2.csv")
    ex_3_2_tables = get_QTables(ex_3_2, "Experiment3_2.csv")
    ex_4_2_tables = get_QTables(ex_4_2, "Experiment4_2.csv")
    ex_5_2_tables = get_QTables(ex_5_2, "Experiment5_2.csv")

    ex_1_2.close()
    ex_2_2.close()
    ex_3_2.close()
    ex_4_2.close()
    ex_5_2.close()

    ex_1_sss_1 = open("Experiment1_SmallStatespace_1.txt", "r")
    ex_2_sss_1 = open("Experiment2_SmallStatespace_1.txt", "r")
    ex_3_sss_1 = open("Experiment3_SmallStatespace_1.txt", "r")
    ex_4_sss_1 = open("Experiment4_SmallStatespace_1.txt", "r")
    ex_5_sss_1 = open("Experiment5_SmallStatespace_1.txt", "r")

    ex_1_sss_1_tables = get_QTables(ex_1_sss_1, "Experiment1_SSS_1.csv")
    ex_2_sss_1_tables = get_QTables(ex_2_sss_1, "Experiment2_SSS_1.csv")
    ex_3_sss_1_tables = get_QTables(ex_3_sss_1, "Experiment3_SSS_1.csv")
    ex_4_sss_1_tables = get_QTables(ex_4_sss_1, "Experiment4_SSS_1.csv")
    ex_5_sss_1_tables = get_QTables(ex_5_sss_1, "Experiment5_SSS_1.csv")

    ex_1_sss_1.close()
    ex_2_sss_1.close()
    ex_3_sss_1.close()
    ex_4_sss_1.close()
    ex_5_sss_1.close()

    ex_1_sss_2 = open("Experiment1_SmallStatespace_2.txt", "r")
    ex_2_sss_2 = open("Experiment2_SmallStatespace_2.txt", "r")
    ex_3_sss_2 = open("Experiment3_SmallStatespace_2.txt", "r")
    ex_4_sss_2 = open("Experiment4_SmallStatespace_2.txt", "r")
    ex_5_sss_2 = open("Experiment5_SmallStatespace_2.txt", "r")

    ex_1_sss_2_tables = get_QTables(ex_1_sss_2, "Experiment1_SSS_2.csv")
    ex_2_sss_2_tables = get_QTables(ex_2_sss_2, "Experiment2_SSS_2.csv")
    ex_3_sss_2_tables = get_QTables(ex_3_sss_2, "Experiment3_SSS_2.csv")
    ex_4_sss_2_tables = get_QTables(ex_4_sss_2, "Experiment4_SSS_2.csv")
    ex_5_sss_2_tables = get_QTables(ex_5_sss_2, "Experiment5_SSS_2.csv")

    ex_1_sss_2.close()
    ex_2_sss_2.close()
    ex_3_sss_2.close()
    ex_4_sss_2.close()
    ex_5_sss_2.close()
    
    os.chdir(orgdir)

def main():
    generate_csv()

main()