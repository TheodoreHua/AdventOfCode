# NOTE: This file is not supported with runner, as the code is not mine

import collections
import sys


def tile_edges(tile):
    return [
        tile[0],
        tile[-1][::-1],
        ''.join(row[-1] for row in tile),
        ''.join(row[0] for row in tile[::-1]),
    ]


def parse_tiles(f):
    tiles = {}
    for line in f:
        tile_id = int(line.partition(':')[0].split()[-1])
        tile = []
        for line in f:
            line = line.strip()
            if not line:
                break
            tile.append(line)
        tiles[tile_id] = tile
    return tiles


def count_edges(tiles):
    edges = collections.Counter()
    for tile in tiles.values():
        edges.update(tile_edges(tile))
    return edges


def count_flipped_edges(tiles):
    edges = collections.Counter()
    for tile in tiles.values():
        edges.update(tile_edges(tile[::-1]))
    return edges


with open("data/input.txt", "r") as f:
    tiles = parse_tiles(f)

if '-v' in sys.argv:
    print(f"{len(tiles)} tiles")

edges = count_edges(tiles)

if '-v' in sys.argv:
    print(f"{len(edges)} unique edges")

edges += count_flipped_edges(tiles)

if '-v' in sys.argv:
    print(f"{len(edges)} unique edges, counting flipping")

if '-v' in sys.argv:
    for tile_id, tile in tiles.items():
        print(f"Tile {tile_id} has these edges:")
        for edge in tile_edges(tile):
            print(f"  {edge} [{'*' * edges[edge]}]")

corner = 1
n_corners = 0
for tile_id, tile in tiles.items():
    # corner tiles have two shared edges and two unique edges
    # other tiles have three or four shared edges
    # (I am assuming at least a 3x3 tile grid!)
    unique = 0
    for edge in tile_edges(tile):
        if edges[edge] == 1:
            unique += 1
        else:
            # just making sure
            assert edges[edge] == 2
    if unique == 2:
        n_corners += 1
        corner *= tile_id
        if '-v' in sys.argv:
            print(f'Corner tile: {tile_id}')

assert n_corners == 4
print(corner)
