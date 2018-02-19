from osmread import parse_file, Way,Node
#import numpy as np
import pickle

filename="map_bits.osm"
cnt=0
node_hash={}
for entity in parse_file(filename):
	if isinstance(entity,Node):
		node_hash[entity.id]=(cnt,entity.lat,entity.lon)
		cnt+=1

adj_list=[]
for _ in range(cnt):
	adj_list.append([])

for entity in parse_file(filename):
	if isinstance(entity,Way):
		n=entity.nodes
		l=len(n)
		'''
		if n[0] in node_hash and n[-1] in node_hash:
			n1=node_hash[n[0]]
			n2=node_hash[n[-1]]
			adj_list[n1].append((n[0],entity.id))
			adj_list[n2].append((n[-1],entity.id))
		'''
		#'''
		for i in range(l-1):
			if n[i] in node_hash and n[i+1] in node_hash:
				n1=node_hash[n[i]][0]
				n2=node_hash[n[i+1]][0]
				#print(adj_list[n1],adj_list[n2])
				adj_list[n1].append((n[i+1],entity.id))
				adj_list[n2].append((n[i],entity.id))
				#print(adj_list[n1],adj_list[n2])
				#print(adj_list)
				#input()
		#'''

print(adj_list)
#input()

with open("node_hash.pickle","wb") as f:
	pickle.dump(node_hash,f)

with open("adj_list.pickle","wb") as f:
	pickle.dump(adj_list,f)
#print(s)
#print(cnt)