import json, sys
h = open(sys.argv[1], 'r')
n = h.readline().strip()
t = int(h.readline().strip())
l = h.readlines()
h.close()
p = []
bi = 1
for L in l:
	s = L.strip().split(" ")
	ta = {}
	if len(s)>2:
		ta["x"] = int(s[1])
		ta["y"] = int(s[2])
	if s[0] == "woodblock" or s[0] == "box":
		ta["type"] = "woodblock"
		ta["w"] = int(s[3])
		ta["h"] = int(s[4])
	elif s[0] == "done":
		ta["type"] = "finish"
	elif s[0] == "ball":
		ta["type"] = "ball"
		ta["id"] = abs(bi-1)
	elif s[0] == "<--":
		ta["type"] = "arrow"
		ta["dir"] = 0
	elif s[0] == "<done>":
		ta["type"] = "finish"
		ta["xv"] = 5
	elif s[0] == "mouse":
		ta["type"] = "moveblock"
		ta["x"] = 0
		ta["y"] = 0
	p.append(ta)
tr = {}
tr["pieces"] = p
tr["time"] = t*2
print json.dumps(tr)
