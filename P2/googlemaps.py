import requests
import pickle
import time

keys=['AIzaSyBNfV7syBGvookzM7YPMwErW2X-9O3NPew','AIzaSyCXtKT6BGweQQa1ZnZ4Wh3W0NGcuACy9nc','AIzaSyBcL2HEjx1LdxHSAI-UXU48UY5IbzIRNhU']
url='https://maps.googleapis.com/maps/api/distancematrix/json'

#sampleurl='https://maps.googleapis.com/maps/api/distancematrix/json?origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key='+key1
end=2803176428
with open("node_hash.pickle","rb") as f:
	node_hash=pickle.load(f)

with open("adj_list.pickle","rb") as f:
	adj_list=pickle.load(f)

distance_matrix=[]
for _ in range(len(adj_list)):
	distance_matrix.append(0)

l=len(adj_list)
factor=23
nodes=list(node_hash.keys())
kn=0
start=198
try:
	for i in range(start,len(nodes)//factor +1):
		orig=''
		for j in range(factor):
			no=i*factor+j
			if no<l:
				no=nodes[no]
				if j==0:
					orig+='{},{}'.format(node_hash[no][1],node_hash[no][2])
				else:
					orig+='|{},{}'.format(node_hash[no][1],node_hash[no][2])
		pa={
			'key':keys[kn],
			'origins':orig,
			'destinations':'{},{}'.format(node_hash[end][1],node_hash[end][2])
		}
		r=requests.get(url,params=pa)
		js=r.json()
		if js['status']!='OK':
			print("Changing key")
			kn+=1
			pa={
				'key':keys[kn],
				'origins':orig,
				'destinations':'{},{}'.format(node_hash[end][1],node_hash[end][2])
			}
			r=requests.get(url,params=pa)
			js=r.json()
		
		#print(js)
		#input()
		j=0
		for r in js['rows']:
			if r['elements'][0]['status']=='NOT_FOUND':
				v=10000
			elif 'duration' in r['elements'][0]:
				v=r['elements'][0]['duration']['value']
			else:
				v=10000
			no=i*factor+j
			distance_matrix[no]=v
			j+=1

		print(i)
		time.sleep(0.5)
finally:
	with open("distance_matrix.pickle","wb") as f:
		pickle.dump(distance_matrix,f)