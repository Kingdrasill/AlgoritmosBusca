import src.maze as mz

def depth_first_search(maze):
  node = mz.ChildNode(maze, None, '')
  node.state = maze.initial_state
  node.path_cost = 0
  frontier = list()
  frontier.append(node)
  explored = list()

  while(True):
    if not frontier:
      return None
    node = frontier.pop()
    if maze.goal_state == node.state:
      return node.Path()
    explored.append(node.state)
    for action in maze.Vizinhos(node.state):
      child = mz.ChildNode(maze, node, action)
      if (child.state not in explored) and (next((x for x in frontier if x.state == child.state), None) == None):
        frontier.append(child)

def breadth_first_search(maze):
  node = mz.ChildNode(maze, None, '')
  if maze.goal_state == node.state:
    return node.Path()
  frontier = list()
  frontier.append(node)
  explored = list()

  while(True):
    if not frontier:
      return None
    node = frontier.pop(0)
    explored.append(node.state)
    for action in maze.Vizinhos(node.state):
      child = mz.ChildNode(maze, node, action)
      if (child.state not in explored) and (next((x for x in frontier if x.state == child.state), None) == None):
        if maze.goal_state == child.state:
          return child.Path()
        frontier.append(child)

def greedy_best_first_search(maze):
  node = mz.ChildNode(maze, None, '')
  frontier = list()
  frontier.append(node)
  explored = list()

  while(True):
    if not frontier:
      return None
    node = frontier.pop(0)
    if maze.goal_state == node.state:
      return node.Path()
    explored.append(node.state)
    for action in maze.Vizinhos(node.state):
      child = mz.ChildNode(maze, node, action)
      if (child.state not in explored) and (next((x for x in frontier if x.state == child.state), None) == None):
        frontier.append(child)
      else:
        for x in frontier:
          if x.state == child.state and x.path_cost > child.path_cost:
            x.parent = child.parent
            x.action = child.action
            x.path_cost = child.path_cost
            break
    frontier.sort(key=lambda x: x.heuristica)

def a_estrela_search(maze):
  node = mz.ChildNode(maze, None, '')
  frontier = list()
  frontier.append(node)
  explored = list()

  while(True):
    if not frontier:
      return None
    node = min(frontier,key=lambda x: x.heuristica + x.path_cost)
    frontier.remove(node)
    if maze.goal_state == node.state:
      return node.Path()
    explored.append(node.state)
    for action in maze.Vizinhos(node.state):
      child = mz.ChildNode(maze, node, action)
      if (child.state not in explored) and (next((x for x in frontier if x.state == child.state), None) == None):
        frontier.append(child)
      else:
        for x in frontier:
          if x.state == child.state and x.path_cost > child.path_cost:
            x.parent = child.parent
            x.action = child.action
            x.path_cost = child.path_cost
            break