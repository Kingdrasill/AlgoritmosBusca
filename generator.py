from pyamaze import maze

size = 10

for i in range(100):
    f = open(f"mazes/maze-{i+1}.txt", "w")
    m = maze(size,size)
    m.CreateMaze(size,size, loopPercent=10)
    string = ""
    for key in m.maze_map.keys():
        string += f"'{key[0]}-{key[1]}' & {m.maze_map[key]} $ "
    string = string[:-2]
    f.write(string)
    f.close()
    del m