import re
from itertools import product
from pathlib import Path

import svgwrite

BOARD_SIZE = ("200", "200")
CSS_STYLES = """
    .background { fill: white; }
    .line { stroke: firebrick; stroke-width: .1mm; }
    .start { fill: green; }
    .dropoff { fill: red; }
    .pickup { fill: blue; }
    .normal {fill: white; }
    rect {
       stroke: black;
       stroke-width: 1;
    }

    .agent {
      r: 10%;
      fill: black;
      stroke-width: 2;
      stroke: grey;
      animation: blinker 4s linear infinite;
      animation: move 5s ease forwards;
    }
    @keyframes blinker {
       50% {
         opacity: 1.0;
       }

    }
"""


def get_movement_data(x_list, y_list, text_path):
    # path_ = path
    x_list_ = x_list
    y_list_ = y_list

    txt = Path(text_path).read_text()

    regex_x = r"\t+\((\d)"
    regex_y = r"\t+\(\d\S\s(\d)"
    matches_x = re.finditer(regex_x, txt, re.MULTILINE)
    move_x = []
    for matchNum, match in enumerate(matches_x, start=1):
        # print("{match}".format(match=match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            move_x.append(int(match.group(groupNum)))

    matches_y = re.finditer(regex_y, txt, re.MULTILINE)
    move_y = []
    for matchNum, match in enumerate(matches_y, start=1):
        # print("{match}".format(match=match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            move_y.append(int(match.group(groupNum)))
    # print(move_y)
    x_list = move_x
    y_list = move_y

    return x_list, y_list


def draw_board(n=3, tile2classes=None):
    dwg = svgwrite.Drawing(size=(f"{n + 0.05}cm", f"{n + 0.05}cm"))

    dwg.add(dwg.rect(size=('100%', '100%'), class_='background'))

    def group(classname):
        return dwg.add(dwg.g(class_=classname))

    # draw squares
    for x, y in product(range(n), range(n)):
        cell = {
            'insert': (f"{x + 0.1}cm", f"{y + 0.1}cm"),
            'size': (f"0.9cm", f"0.9cm"),
        }
        if tile2classes is not None and tile2classes(x, y):
            cell["class_"] = tile2classes(x, n - y - 1)
        cz = x + 0.50
        cv = (y - 1.35)
        print(x, y)
        if (x == 2) and (y == 4):
            print(cz, cv)
            dwg.add(dwg.text('P', insert=(f"{cz}cm", f"{cv}cm"), fill='white'))
        if (x == 2) and (y == 2):
            print(cz, cv)
            dwg.add(dwg.text('P', insert=(f"{cz}cm", f"{cv}cm"), fill='white'))
        if (x == 4) and (y == 0):
            cz = 4.5
            cv = 2.65
            dwg.add(dwg.text('P', insert=(f"{cz}cm", f"{cv}cm"), fill='black'))
            print(cz, cv)
        dwg.add(dwg.rect(**cell))

    return dwg


def gen_offsets(actions):
    dx, dy = 0, 0
    for ax, ay in actions:
        dx = ax
        dy = ay
        yield dx, dy


def move_keyframe(dx, dy, ratio):
    return f"""{ratio * 100}% {{
    transform: translate({dx}cm, {dy}cm);
}}"""


def gridworld(n=5, actions=None, tile2classes=None, extra_css=""):
    dwg = draw_board(n=n, tile2classes=tile2classes)

    css_styles = CSS_STYLES
    if actions is not None:
        # Add agent.
        x, y = 0, 4  # start position.
        cx, cy = x + 0.55, (n - y - 1) + 0.55
        dwg.add(svgwrite.shapes.Circle(
            r="0.1cm",
            center=(f"{cx}cm", f"{cy}cm"),
            class_="agent",
        ))
        # dwg.add(svgwrite.shapes.Line(
        #     start=({cx},{cy}),
        #     class_="path",
        # ))

        offsets = gen_offsets(actions)
        keyframes = [move_keyframe(x, y, (i + 1) / len(actions)) for i, (x, y)
                     in enumerate(offsets)]
        move_css = "\n@keyframes move {\n" + '\n'.join(keyframes) + "\n}"
        css_styles += move_css

    dwg.defs.add(dwg.style(css_styles + extra_css))
    return dwg


if __name__ == '__main__':
    def tile2classes(x, y):
        if (x == 0) and (y == 4):
            return "start"
        elif (x == 2) and (y == 4):
            return "pickup"
        elif (x == 2) and (y == 2):
            return "pickup"
        elif (x == 4) and (y == 0):
            return "pickup"
        elif (x == 0) and (y == 0):
            return "dropoff"
        elif (x == 2) and (y == 0):
            return "dropoff"
        elif (x == 4) and (y == 3):
            return "dropoff"
        return "normal"


    x = []
    y = []
    experiment_paths = [
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment1_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment1_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment1_SmallStatespace_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment1_SmallStatespace_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment2_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment2_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment2_SmallStatespace_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment2_SmallStatespace_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment3_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment3_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment3_SmallStatespace_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment3_SmallStatespace_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment4_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment4_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment4_SmallStatespace_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment4_SmallStatespace_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment5_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment5_2.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment5_SmallStatespace_1.txt",
        "/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment5_SmallStatespace_2.txt"
    ]
    for paths in experiment_paths:
        x, y = get_movement_data(x, y, paths)
        actions = []
        for x_, y_ in zip(x, y):
            actions.append((x_, y_))
            dwg = gridworld(n=5, tile2classes=tile2classes, actions=actions)
            dwg.saveas("example.svg", pretty=True)
