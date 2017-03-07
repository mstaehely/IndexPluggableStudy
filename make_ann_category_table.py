#!/usr/bin/env python3

import collections

with open("combined_analysis.txt", 'r') as f:
    lines = f.readlines()

categories = collections.defaultdict(int)
counted_total = 0
section_total = 0
for line in lines:
    line = line.rstrip()
    if line.startswith("Total- "):
        total = int(line[7:])
    elif line.startswith("    "):
        line = line[4:]
        if line.startswith("Other- "):
            assert line.endswith(" (main)")
            count = int(line[len("Other- "):-len(" (main)")])
            categories["Other (main)"] += count
            counted_total += count
        else:
            category, count = line.split('- ')
            count = int(count)
            categories[category] += count
            counted_total += count
    elif line.startswith("Override parameter invalid- "):
        assert line.endswith(" total")
        override_param_inval = int(line[len("Override parameter invalid- "):-len(" total")])
        categories["Override parameter invalid"] += override_param_inval
    elif line.startswith("Cast Suppression- "):
        assert line.endswith(" total")
        cast_suppression = int(line[len("Cast Suppression- "):-len(" total")])
        categories["Cast Suppression"] += cast_suppression
    elif line.endswith(" total"):
        assert counted_total == section_total, ("Section before this: " + line)
        section_total = int(line.split()[-2])
        counted_total = 0
assert section_total == counted_total
categories = dict(categories)

assert total == sum(categories.values())

print("Result of partial/period inheritance- {}".format(categories["Array factory trouble"] + categories["Result of partial/period"] + categories["Unable to guarantee"]))
print("Unary~- {}".format(categories["Bitwise operation"] - 1))
print("Calls to size()- {}".format(categories["Result of size() call"]))
print("Index arithmetic- {}".format(categories["Index arithmetic"]))
print("Potentially null arrays- {}".format(categories["Inability to verify array exists at runtime"]))
print("Usage of constants- {}".format(categories["Unable to annotate constants"]))
print("Variable array lengths- {}".format(categories["Variable array length"] + categories["Array length guarantees"]))
print("Can't express guarantee- {}".format(categories["Can't express guarantee"]))
print("Size initialized before array- {}".format(categories["Size before array"]))
print("Usage of array by main method- {}".format(categories["Other (main)"]))
print("Arithmetic guarantee of correctness- {}".format(categories["Arithmetic guarantee"]))
print("Unsupported library in JDK- {}".format(categories["Unsupported JDK"]))
print("Override parameter invalid- {}".format(categories["Override parameter invalid"]))
print("Argument incompatible- {}".format(categories["Incompatible"]))
print("Cast warning- {}".format(categories["Cast Suppression"]))
print("Checker unable to follow reference- {}".format(categories["Unable to chase references"]))
print("Unary&- {}".format(1))

## import pprint
## pprint.pprint(categories)

