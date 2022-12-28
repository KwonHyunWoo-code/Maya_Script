def UVToMesh(obj, Origin, Facing, Scale):


	bounds = cmds.polyEvaluate(obj, boundingBox = True)

	# If scale is 0, calculated scale factor from object area.
	if(Scale == 0):
		Area = cmds.polyEvaluate(obj, area = True)
		Scale = sqrt(Area)

	# If origin is 0, unfold will be placed next to object.
	# If origin is 1, unfold will be placed at world center.

	Center = cmds.xform(obj, q = True, a = True, ws = True, rp = True)

	if (Origin == 1):
		Center = [0, 0, 0]
		bounds = [(0, 0), (0, 0), (0, 0)]
		cmds.xform(obj, a = True, ws = True, rp = (0, 0, 0))

	numUVs = cmds.polyEvaluate(obj, uv = True)

	cmds.progressWindow(t = "mopKnit", pr = 0, max = numUVs, st = ("Processing" + "\n"+ obj + "\n" +"..."), isInterruptable = True)

	i = 0
	while i < numUVs:

		uvPos = cmds.polyEditUV(obj + ".map[" + str(i) + "]", q=True)
		geoVert = cmds.polyListComponentConversion(obj + ".map[" + str(i) + "]", fuv = True, tv = True)

		if(Facing == "X" or Facing == "x"):
			cmds.xform(geoVert, a=True, ws=True, t=
				(bounds[0][1], #Offset
				((uvPos[1]-0.5)*Scale)+Center[1], # V-> Y
				((0.5-uvPos[0])*Scale)+Center[2])) # U -> Z , inverse

		elif (Facing == "Y" or Facing == "y"):
			cmds.xform(geoVert, a=True, ws=True, t=				
				(((uvPos[0]-0.5)*Scale)+Center[0], # U-> X
				bounds[1][0], #Offset
				((0.5-uvPos[1])*Scale)+Center[2])) # V -> Z , inverse

		else:
			cmds.xform(geoVert, a=True, ws=True, t=
				(((uvPos[0]-0.5)*Scale)+Center[0], # U -> X
				((uvPos[1]-0.5)*Scale)+Center[1], # V -> Y
				bounds[2][0]) # Offset.

		cmds.progressWindow(edit=True, progress=i)

		i += 1

	cmds.progressWindow(endProgress=True)