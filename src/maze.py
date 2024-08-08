class ChildNode:
  def __init__(self, maze, parent, direction):
    tmp_state = maze.PegarVizinho(parent, direction)
    self.state = tmp_state if tmp_state != None else maze.initial_state
    self.parent = parent
    self.action = direction
    self.heuristica = ((maze.goal_state[0] - self.state[0])**2 + (maze.goal_state[1] - self.state[1])**2)**(1/2)
    self.path_cost = (maze.custo_mover + parent.path_cost) if tmp_state != None else 0
    
  def __str__(self):
    string = "Node:\n"
    string += f"State: {self.state}\n"
    string += f"Parent: {self.parent}\n"
    string += f"Action: {self.action}\n"
    string += f"Path_Cost: {self.path_cost}"
    return string
  
  def Path(self):
    path = list()
    no = self
    while(True):
      path.append(no.state)
      if no.parent == None:
        break
      no = no.parent
    path.reverse()
    return path

class Maze:
  def __init__(self, maze, size, custo, inicial, final, ordem):
    self.maze = maze
    self.size = size
    self.initial_state = inicial
    self.goal_state = final
    self.custo_mover = custo
    self.actions = ordem

  def __str__(self):
    string = "Labirinto(Grafo):\n"
    string += f"Estado Inicial: {self.initial_state}\n"
    string += f"Estado Objetivo: {self.goal_state}\n"
    for node in self.maze.keys:
      string += f'{node}: {self.maze[node]}'
      string += "\n"
    return string

  def PegarVizinho(self, node, direction):
    neighbour = None
    if node != None:
      match(direction):
          case 'N':
            neighbour = (node.state[0]-1, node.state[1])
            pass
          case 'S':
            neighbour = (node.state[0]+1, node.state[1])
            pass
          case 'W':
            neighbour = (node.state[0], node.state[1]-1)
            pass
          case 'E':
            neighbour = (node.state[0], node.state[1]+1)
            pass
    return neighbour

  def Vizinhos(self, node):
    vizinhos = []
    for o in self.actions:
      match(o):
        case 'N':
          if self.maze[node]['N']:
            vizinhos.append('N')
          pass
        case 'S':
          if self.maze[node]['S']:
            vizinhos.append('S')
          pass
        case 'W':
          if self.maze[node]['W']:
            vizinhos.append('W')
          pass
        case 'E':
          if self.maze[node]['E']:
            vizinhos.append('E')
          pass
    return vizinhos