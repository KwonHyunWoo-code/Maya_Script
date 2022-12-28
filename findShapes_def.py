def findShapes(obj):
shapes = cmds.listRelatives(obj, f = True, s = True, ni = True)
found = 0
for shape in shapes:
	if cmds.nodeType(shape) == "mesh":
		found = 1

return found