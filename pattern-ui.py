"""
Testing UI for pattern.py. Demonstrates one way to:
1) print pattern tree with formatting
2) access pattern functioncs dynamically
"""

import pattern

TAB_STR = "\t"

def pattern_ui(pattern_name):
    getattr(pattern,pattern_name)()
    for x in pattern.pattern_tree:
        print TAB_STR*x['indent'] + "[" + x['name'] + "] x%d" % (x['quan'])
    pattern.pattern_tree = []
