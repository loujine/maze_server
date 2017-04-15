import os

# Rels for links below
labels = {
    'north': "North",
    "east": "East",
    "south": "South",
    "west": "West",
    "exit": "Exit"
}
rels = ['north', 'east', 'south', 'west', 'exit']

directions = {
    'north': ['west', 'north', 'east', 'south'],
    'east': ['north', 'east', 'south', 'west'],
    'south': ['east', 'south', 'west', 'north'],
    'west': ['south', 'west', 'north', 'east'],
    'exit': ['west', 'north', 'east', 'south'],
}

# Each cell and it's links to the other cells
# The items of each cell correspond to the rel above
cells = [
    [1, None, None, None, None],
    [None, 6, 0, None, None],
    [None, 7, 3, None, None],
    [2, None, 4, None, None],
    [3, 9, None, None, None],
    [None, 10, None, 0, None],
    [None, None, 7, 1, None],
    [6, 12, None, 2, None],
    [None, 13, 9, None, None],
    [8, None, None, 4, None],
    [None, None, 11, 5, None],
    [10, 16, None, None, None],
    [None, None, None, 7, None],
    [None, None, 14, 8, None],
    [13, 19, None, None, None],
    [None, 20, None, None, None],
    [None, 21, None, 11, None],
    [None, 22, 18, None, None],
    [17, None, 19, None, None],
    [18, 24, None, 14, None],
    [None, None, 21, 15, None],
    [20, None, 22, 16, None],
    [21, None, None, 17, None],
    [None, None, 24, None, None],
    [None, None, None, None, 999]
]

mini_maze = [
    [1, None, None, None, None],
    [None, 2, None, None, None],
    [3, None, None, None, None],
    [None, None, None, None, 999],
]
cells = mini_maze

def link_to_cell(cell_num, direction):
    """
    Helper for generating links to specific cells
    """
    base_iri = os.environ.get("BASE_IRI", "http://127.0.0.1:5000")
    return '{base_iri}/cells/{cell_num}/{direction}'.format(**locals())

def has_cell(cell_num):
    return cell_num <= len(cells) - 1

def get_links_for_cell(cell_num):
    """
    Generates link for a specific cell
    """
    cell = cells[cell_num]
    cell_with_rels = dict(zip(rels, cell))
    links = dict((k, link_to_cell(v, directions[k][1]))
                 for k, v in cell_with_rels.iteritems() if v)
    return links
