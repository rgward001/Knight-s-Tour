from graph import Graph, Node
from a_star import AStar
import numpy as np


def run():
    bdSize = int(input("Enter a board size: "))
    start = input(f"Please enter a number between 0 and {(bdSize**2)-1} to start: ")
    target = input(f"Please enter a number between 0 and {(bdSize**2)-1} to finish: ")
    # Create graph
    graph = Graph()
    visual = np.zeros((bdSize, bdSize))
    visualpath = []
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = str(posToNodeId(row, col, bdSize))
            newPositions = genLegalMoves(row, col, bdSize)
            if graph.find_node(posToNodeId) == None:
              graph.add_node(Node(nodeId, (row,col)))
            for i in newPositions:
              newX = i[0]
              newY = i[1]
              nid = str(posToNodeId(newX, newY, bdSize))
              if graph.find_node(nid) == None:
                graph.add_node(Node(nid, (newX,newY)))
              graph.add_edge(nodeId, nid)
      
    # Execute the algorithm
    alg = AStar(graph, start, target)
    path, path_length = alg.search()
    for i in graph.nodes:
      if i in path:
        visualpath.append(i)
    for r in visualpath:
      visual[r.x, r.y] = 1
    print(" -> ".join(path))
    print(f"Length of the path: {int(path_length/2)}")
    print(visual)
    

def posToNodeId(row, col, bdSize):
    return (row * bdSize) + col

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                           (1, -2), (1, 2), (2, -1), (2, 1)]
    for item in moveOffsets:
        newX = x + item[0]
        newY = y + item[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


if __name__ == '__main__':
    run()

