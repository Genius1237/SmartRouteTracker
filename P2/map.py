from osmread import parse_file, Way,Node
#import numpy as np
import pickle

cnt=0
node_hash={}
for entity in parse_file('map_2.osm'):
	if isinstance(entity,Node):
		node_hash[entity.id]=cnt
		cnt+=1

adj_list=[]
for _ in range(cnt):
	adj_list.append([])

for entity in parse_file('map_2.osm'):
	if isinstance(entity,Way):
		n=entity.nodes
		l=len(n)
		for i in range(l-1):
			if n[i] in node_hash and n[i+1] in node_hash:
				n1=node_hash[n[i]]
				n2=node_hash[n[i+1]]
				#print(adj_list[n1],adj_list[n2])
				adj_list[n1].append((n[i+1],entity.id))
				adj_list[n2].append((n[i],entity.id))
				#print(adj_list[n1],adj_list[n2])
				#print(adj_list)
				#input()

with open("node_hash.pickle","wb") as f:
	pickle.dump(node_hash,f)

with open("adj_list.pickle","wb") as f:
	pickle.dump(adj_list,f)
#print(s)
#print(cnt)