import src.search as sc
import time as tm
import tracemalloc as tr
import ast as at

methods = {
    'DFS': sc.depth_first_search,
    'BFS': sc.breadth_first_search,
    'GBF': sc.greedy_best_first_search,
    'A*': sc.a_estrela_search
}
datas = {}
files = 100
for i in range(files):
    file = open(f"mazes/maze-{i+1}.txt", "r")
    labirinto = {}
    nodes = file.read().split('$')
    for node in nodes:
        node = node.replace(' ', '')
        items = node.split('&')
        key = (items[0])[1:-1].split('-')
        key = (int(key[0]), int(key[1]))
        value = at.literal_eval(items[1])
        labirinto.update({key: value})
    file.close()

    datas.update({i+1: {}})

    for method in methods:    
        maze = sc.mz.Maze(labirinto, 10, 1, (1,1), (10,10), ['N', 'W', 'E', 'S'])

        tr.start()
        start = tm.time()
        
        path = methods[method](maze)
        
        end = tm.time()
        memory_used = tr.get_traced_memory()
        tr.stop()

        exec_time = end - start
        
        datas[i+1].update({method: {
          'time': exec_time * 1000,
          'memory': memory_used[1],
          'path': path  
        }})

        del maze
        del path
        del start
        del end
        del exec_time
    del file
    del labirinto

times = {}
memories = {}
completudes = {}
optimalities = {}
for maze in datas:
    for method in datas[maze]:
        times.update({method: 0})
        memories.update({method: 0})
        completudes.update({method: 0})
        optimalities.update({method: 0})


# Print averages
for maze in datas:
    for method in datas[maze]:
        times.update({method: (times[method] + datas[maze][method]['time'])})
        memories.update({method: (memories[method] + datas[maze][method]['memory'])})
        if datas[maze][method]['path'] != None:
            completudes.update({method: (completudes[method] + 1)})

for maze in datas:
    size_paths = []
    for method in datas[maze]:
        if datas[maze][method]['path'] != None:
            size_paths.append((method, len(datas[maze][method]['path'])))
    minimum = min(size_paths, key=lambda x: x[1])[1]
    for method in datas[maze]:
        if datas[maze][method]['path'] != None:
            if len(datas[maze][method]['path']) == minimum:
                optimalities.update({method: (optimalities[method] + 1)})

for method in times:
    times.update({method: (times[method] / files)})
    memories.update({method: (memories[method] / files)})
    completudes.update({method: (completudes[method] / files * 100)})
    optimalities.update({method: (optimalities[method] / files * 100)})

print(times)
print(memories)
print(completudes)
print(optimalities)