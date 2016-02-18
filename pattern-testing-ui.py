"""
Testing UI for pattern.py. Demonstrates one way to:
1) print pattern tree with formatting
2) access pattern functioncs dynamically

Reminder: When you call pattern_ui, the pattern_name argument
must be submitted in quotes ('quartz' NOT quartz).
"""

import pattern

TAB_STR = "\t"

def pattern_ui(pattern_name,quan=1,indent=0):
    getattr(pattern,pattern_name)(quan,indent)
    for x in pattern.pattern_tree:
        print TAB_STR*x['indent'] + "[" + x['name'] + "] x%d" % (x['quan'])
    pattern.pattern_tree = []
