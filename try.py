graph = { "0" : ["1","3"],
          "1" : ["2", "4","0"],
          "2" : ["1", "5"],
          "3" : ["0","4","6"],
          "4" : ["1", "3","5","7"],
          "5" : ["2","4","8"],
          "6" : ["3","9","7"],
          "7" : ["4","6","8","10"],
          "8" : ["5","7","11"],
          "9" : ["6","10","12"],
          "10" : ["7","9""11","13"],
          "11" : ["8","10","14"],
          "12" : ["9","13","15"],
          "13" : ["10","12","14","16"],
          "14" : ["11","13","17"],
          "15" : ["12","16","18"],
          "16" : ["13","15","17","19"],
          "17" : ["14","16","20"],
          "18" : ["15","19","21"],
          "19" : ["16","18","20","22"],
          "20" : ["17","19","23"],
          "21" : ["18","22","24"],
          "22" : ["19","21","23","25"],
          "23" : ["20","22","26"],
          "24" : ["21","25"],
          "25" : ["24","22","26"],
          "26" : ["25","23"],
          }

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return False
        if not graph.has_key(start):
            return True
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                        return newpath
        return None

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

#print(generate_edges(graph))

def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

print find_path(graph, "1", "5")

