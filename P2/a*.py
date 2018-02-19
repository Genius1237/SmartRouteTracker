import heapq
import pickle
import numpy as np
from igraph import *
import sys
with open("node_hash.pickle","rb") as f:
	node_hash = pickle.load(f)
with open("adj_list.pickle","rb") as f:
	adj_list = pickle.load(f)
with open("distance_matrix.pickle","rb") as f:
	distance_matrix = pickle.load(f)

def heuristic_func(node):
	return distance_matrix[node_hash[node][0]]

def children(node):
	n = node_hash[node][0]
	return [e[0] for e in adj_list[n]]

open_list_depth={}
closed_list={}
parent={}

def AStarFunc(start,end = 2803176428):
	open_list = []
	d=0
	heapq.heappush(open_list,(heuristic_func(start),start))
	open_list_depth[start]=d

	curr_loc = start
	parent[start]=-1
	while open_list:
		_,curr_loc = heapq.heappop(open_list)
		d = open_list_depth[curr_loc]
		del open_list_depth[curr_loc]

		if curr_loc == end:
			print(d)
			path=[end]
			path1=[node_hash[end][0]]
			i=0
			node=end
			while True:
				pa=parent[node]
				if pa==-1:
					break
				else:
					path.insert(0,pa)
					path1.insert(0,node_hash[pa][0])
					node=pa

			print(path1)
			'''
			a=np.zeros((len(adj_list),len(adj_list)))
			for i in range(len(adj_list)):
				for j in range(len(adj_list[i])):
					a[i][node_hash[adj_list[i][j][0]][0]]=1

			g = Graph.Adjacency(a.tolist())
			
			#keys=node_hash.keys()
			names=[]
			#for key in node_hash:
				#names.insert(node_hash[key][0],'{},{}'.format(node_hash[key][1],node_hash[key][2]))
			#names.insert(0,'{},{}'.format(node_hash[n][1],node_hash[n][2]))
			#print(names)

			#	g.vs["name"] = names
			layout = g.layout("kk")
			visual_style = {}
			visual_style["vertex_size"] = [30]
			visual_style["vertex_label"] = [a for a in g.vs["name"]]
			color_dict = {"0":"red"}
			g.vs["color"] = color_dict["0"]
			visual_style["edge_arrow_size"]=4
			visual_style["vertex_label_size"]=30
			visual_style["layout"] = layout
			visual_style["bbox"] = (3500, 3500)
			visual_style["margin"] = 300
			visual_style["edge_width"] = 4
			plot(g, **visual_style)
			'''
			#'''
			nnn=0
			for n in path:
				no =len(adj_list[node_hash[n][0]])+1
				a=np.zeros((no,no))
				for i in range(no-1):
					a[0][i+1]=1

				g = Graph.Adjacency(a.tolist())
				names=['{}\n{}\n{}'.format(node_hash[i[0]][0],node_hash[i[0]][1],node_hash[i[0]][2]) for i in adj_list[node_hash[n][0]]]
				names.insert(0,'{}\n{}\n{}'.format(node_hash[n][0],node_hash[n][1],node_hash[n][2]))
				color_dict = {0:"red",1:"green"}
				colors=[color_dict[1]]
				for i in range(no-1):
					if nnn-1>=0 and path[nnn-1]==adj_list[node_hash[n][0]][i][0]:
						colors.append(color_dict[1])
					elif nnn+1<len(path) and path[nnn+1]==adj_list[node_hash[n][0]][i][0]:
						colors.append(color_dict[1])
					else:
						colors.append(color_dict[0])

				#print(names)

				g.vs["name"] = names
				layout = g.layout("kk")
				visual_style = {}
				visual_style["vertex_size"] = [300]
				visual_style["vertex_label"] = [a for a in g.vs["name"]]
				g.vs["color"] = colors
				#visual_style["edge_arrow_size"]=4
				visual_style["vertex_label_size"]=75
				visual_style["layout"] = layout
				visual_style["bbox"] = (3500, 3500)
				visual_style["margin"] = 300
				visual_style["edge_width"] = 4
				plot(g, **visual_style)
				nnn+=1
			#'''
			exit()
		else:
			for child in children(curr_loc):
				if child in open_list_depth:
					if open_list_depth[child] > d+1:
						open_list_depth[child] = d+1
						parent[child]=curr_loc

				elif child in closed_list:
					if closed_list[child] > d+1:
						open_list_depth[child] = d+1
						del closed_list[child]
						heapq.heappush(open_list,(heuristic_func(child),child))
						parent[child]=curr_loc

				else:
					heapq.heappush(open_list,(heuristic_func(child),child))
					open_list_depth[child]=d+1
					parent[child]=curr_loc

		closed_list[curr_loc] = d


def main():
	start = 2684820160
	AStarFunc(start)


if __name__ == '__main__':
	main()
