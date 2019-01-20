import time
from ucs.graph import *
from ucs.priority_queue import *
from mapGeneratorPygame.mapGenerator import returnMapWithBombs
import random

graphNodes = []
bombMaps = returnMapWithBombs()[0]
bombMatrix = returnMapWithBombs()[1]
posList = []
randWeightList = []
tmp = []
tmpGraph = Graph()
parent = (-1,-1)

def run(graph, key_node_start, key_node_goal, verbose=False, time_sleep=0):
	if key_node_start not in graph.getNodes() or key_node_goal not in graph.getNodes():
		print('Error: key_node_start \'%s\' or key_node_goal \'%s\' not exists!!' % (key_node_start, key_node_goal))
	else:
		# UCS uses priority queue, priority is the cumulative cost (smaller cost)
		queue = PriorityQueue()

		# expands initial node

		# get the keys of all successors of initial node
		keys_successors = graph.getSuccessors(key_node_start)
		parent = key_node_start
		tmpGraph.addNode(parent)

		# adds the keys of successors in priority queue
		for key_sucessor in keys_successors:
			weight = graph.getWeightEdge(key_node_start, key_sucessor)
			# each item of queue is a tuple (key, cumulative_cost)
			queue.insert((key_sucessor, weight), weight)
			tmpGraph.addNode(key_sucessor)
			tmpGraph.connect(parent, key_sucessor, 1)



		reached_goal, cumulative_cost_goal = False, -1
		while not queue.is_empty():
			# remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
			key_current_node, cost_node = queue.remove() 
			if(key_current_node == key_node_goal):
				if not tmpGraph.isKeyExist(key_current_node):
					tmpGraph.addNode(key_current_node)
				tmpGraph.connect(parent, key_current_node, 1)
				reached_goal, cumulative_cost_goal = True, cost_node
				break

			if verbose:
				# shows a friendly message
				print('Expands node \'%s\' with cumulative cost %s ...' % (key_current_node, cost_node))
				graphNodes.append((key_current_node, cost_node))
				tmp.append((key_current_node,parent))
				# if not tmpGraph.isKeyExist(key_current_node):
				# 	tmpGraph.addNode(key_current_node)
				# tmpGraph.connect(parent,key_current_node,1)

				time.sleep(time_sleep)

			# get all successors of key_current_node
			keys_successors = graph.getSuccessors(key_current_node)
			parent = key_current_node

			if keys_successors: # checks if contains successors
				# insert all successors of key_current_node in the queue
				for key_sucessor in keys_successors:
					cumulative_cost = graph.getWeightEdge(key_current_node, key_sucessor) + cost_node
					queue.insert((key_sucessor, cumulative_cost), cumulative_cost)
					if not tmpGraph.isKeyExist(key_sucessor):
						tmpGraph.addNode(key_sucessor)
					tmpGraph.connect(parent, key_sucessor, 1)

		if(reached_goal):
			print('\nReached goal! Cost: %s\n' % cumulative_cost_goal)
			# for row in graphNodes:
			# 	print(row)
		else:
			print('\nUnfulfilled goal.\n')


if __name__ == "__main__":

	# build the graph...
	# adds nodes in the graph
	graph = Graph()

	for x in range(10):
		for y in range(10):
			graph.addNode((x, y))
	for node in graph.nodes:
		print(node)

	for x in range(10):
		for y in range(10):
			if y < 9 :
				print((x,y),' => ', (x,y+1))
				graph.connect((x,y),(x,y+1),1)
				graph.connect((x, y + 1), (x, y), 1)
			if x < 9 :
				print((x, y), ' => ', (x+1, y))
				graph.connect((x, y), (x+1, y), 1)
				graph.connect((x + 1, y), (x, y), 1)
	for node in graph.nodes:
		print(node, ' -- ', graph.getSuccessors(node))

	run(graph,(4,5),(2,2),True)

	for node in tmpGraph.nodes:
		print('parent ',node , ' have sons ', tmpGraph.getSuccessors(node))

	print([].__len__())
	# smallTmpGraph.addNode((0,0))
	# print('z 00 ',smallTmpGraph.nodes)
	# smallTmpGraph.nodes.pop((0,0))
	# print('bez 00 ', smallTmpGraph.nodes)
	toPop = []

	for node in tmpGraph.nodes:
		if  node != (2,2) and tmpGraph.getSuccessors(node).__len__() == 0:
			toPop.append(node)
	for node in toPop:
		tmpGraph.nodes.pop(node)
		tmpGraph.removeConnection(node)
	# for node in tmpGraph.nodes:
	# 	for successor in tmpGraph.getSuccessors(node):
	# 		for target in toPop:
	# 			if target==successor:
	# 				print('to Pop ',successor)
	for node in tmpGraph.nodes:
		print('parent ',node , ' have sons ', tmpGraph.getSuccessors(node))

	toPop = []
	print('================================')

	for node in tmpGraph.nodes:
		for successor in tmpGraph.getSuccessors(node):
			if not tmpGraph.isKeyExist(successor):
				toPop.append(node)
	print(toPop)
	for node in toPop:
		tmpGraph.nodes.pop(node)
		tmpGraph.removeConnection(node)
	# for node in tmpGraph.nodes:
	# 	for successor in tmpGraph.getSuccessors(node):
	# 		for target in toPop:
	# 			if target==successor:
	# 				print('to Pop ',successor)
	for node in tmpGraph.nodes:
		print('parent ', node, ' have sons ', tmpGraph.getSuccessors(node))





	# for node in tmp:
	# 	print('parent ',node[1], ' have son ',node[0])

	# if not graph.isKeyExist((-1,-1)):
	# 	print('ni ma')





	# graph.addNode((0, 0))
	# posList.append((0, 0, 1))
	#
	# for i in range(10):
	# 	randWeight = random.randrange(1, 50)
	# 	randWeightList.append(randWeight)
	#
	# for i in range(10):
	# 	graph.addNode((bombMaps[i][0], bombMaps[i][1]))
	# 	posList.append((bombMaps[i][0], bombMaps[i][1], (bombMaps[i][0] + bombMaps[i][1]) * randWeightList[i]))
	#
	# graph.addNode((9, 9))
	#
	# print(graph.nodes)
	#
	# print('not sorted yet')
	# for row in posList:
	# 	print(row)
	#
	# posList.sort(key=lambda x: x[2])
	#
	# print('all sorted')
	# for row in posList:
	# 	print(row)
	#
	# posList.append((9, 9, 1))
	#
	# # dopisz Wiktor wagi - Na razie rzuca randomowo
	# # 0 -> 1 | 0 -> 2
	# graph.connect((posList[0][0], posList[0][1]), (posList[1][0], posList[1][1]), posList[1][2])
	# graph.connect((posList[0][0], posList[0][1]), (posList[2][0], posList[2][1]), posList[2][2])
	#
	# # 1 -> 3 | 1 -> 4
	# graph.connect((posList[1][0], posList[1][1]), (posList[3][0], posList[3][1]), posList[3][2])
	# graph.connect((posList[1][0], posList[1][1]), (posList[4][0], posList[4][1]), posList[4][2])
	#
	# # 2 -> 5 | 2 -> 6
	# graph.connect((posList[2][0], posList[2][1]), (posList[5][0], posList[5][1]), posList[5][2])
	# graph.connect((posList[2][0], posList[2][1]), (posList[6][0], posList[6][1]), posList[6][2])
	#
	# # 3 -> 7 | 3 -> 8
	# graph.connect((posList[3][0], posList[3][1]), (posList[7][0], posList[7][1]), posList[7][2])
	# graph.connect((posList[3][0], posList[3][1]), (posList[8][0], posList[8][1]), posList[8][2])
	#
	# # 4 -> 9 | 4 -> 10
	# graph.connect((posList[4][0], posList[4][1]), (posList[9][0], posList[9][1]), posList[9][2])
	# graph.connect((posList[4][0], posList[4][1]), (posList[10][0], posList[10][1]), posList[10][2])
	#
	# #10 -> 11
	# graph.connect((posList[10][0], posList[10][1]), (posList[11][0], posList[11][1]), posList[11][2])
	#
	# # linking the nodes
	# #
	# # x, y = 0, 0
	# # for x in range(10):
	# # 	for y in range(10):
	# # 		graph.addNode((x, y))
	# #
	# # x, y = 0, 0
	# # for y in range(10):
	# # 	for x in range(10):
	# # 		# graph.connect((x, y), (x + 1, y), 1)
	# # 		# graph.connect((x, y), (x, y + 1), 2)
	# # 		print("X: ", x, '  Y: ', y)
	# # 		print(bombMaps[y][0], bombMaps[y][1])
	# # 		if x + 1 == bombMaps[y][0] and y == bombMaps[y][1]:
	# # 			graph.connect((x, y), (x + 1, y), bombMaps[y][2])
	# # 		else:
	# # 			graph.connect((x, y), (x + 1, y), 0)
	# # 			graph.connect((x, y), (x, y + 1), 0)
	#
	# run(graph=graph, key_node_start=(0, 0), key_node_goal=(9, 9), verbose=True, time_sleep=2)
