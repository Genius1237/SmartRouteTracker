import pickle

with open("node_hash.pickle","rb") as f:
	node_hash=pickle.load(f)

with open("adj_list.pickle","rb") as f:
	adj_list=pickle.load(f)

start=2684820160
end=2803176428

assert start in node_hash
assert end in node_hash
visited=[]
for i in range(len(adj_list)):
	visited.append(0)

path=[]
stack=[]

stack.append((start,0))
path.append(start)
currd=0
while len(stack)>=1:
	node,d=stack.pop()
	for _ in range(currd-d):
		path.pop()
	currd=d
	path.append(node)
	n=node_hash[node][0]
	visited[n]=1
	#path.append(node)
	if node==end:
		for e in path:
			print(node_hash[e][1],node_hash[e][2])
		print(len(path))
		exit()

	for el in adj_list[n]:
		if visited[node_hash[el[0]][0]]==0:
			stack.append((el[0],d+1))