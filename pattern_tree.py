# pylint: disable=missing-docstring

"""
Part of the pattern calculator for Drakor.
"""

tree = [] # pylint: disable=invalid-name

def build_tree(mat_name, quantity, indent):
    tree.append({'name':mat_name, 'quan':quantity, 'indent':indent})
