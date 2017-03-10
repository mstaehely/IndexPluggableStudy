#!/usr/bin/env python3

import collections
import sys

lines = sys.stdin.readlines()

group = None
annotation_lines = []
total_annotations = 0
suppression_lines = []
total_suppressions = 0
general_suppression_lines = []
total_general_suppressions = 0
for line in lines:
    line = line.rstrip()
    if line.startswith("Files:"):
        print(line)
    elif line.startswith("Array uses: "):
        print(line)
    elif line == "Annotations:":
        group = "Annotations"
    elif line == "Suppressions:":
        group = "Suppressions"
    elif line == "General Suppressions:":
        group = "General Suppressions"
    elif line == "":
        pass
    elif group == "Annotations":
        annotation_lines.append(line)
        total_annotations += int(line.split(': ')[1])
    elif group == "Suppressions":
        suppression_lines.append(line)
        total_suppressions += int(line.split(': ')[1])
    elif group == "General Suppressions":
        general_suppression_lines.append(line)
        total_general_suppressions += int(line.split(': ')[1])
    else:
        assert False

print()
print()
print("Annotations: {}".format(total_annotations))
for line in annotation_lines:
    print(line)
print()
print()
print("Suppressions: {}".format(total_suppressions))
for line in suppression_lines:
    print(line)
# print()
# print()
# print("General Suppressions: {}".format(total_general_suppressions))
# for line in general_suppression_lines:
#     print(line)

