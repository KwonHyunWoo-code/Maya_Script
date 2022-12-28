def splitMeshUVs(obj):
	uvBorder = []
	edgeUVs = []
	finalBorder = []

	cmds.select(obj + ".map[*]", r = True)
	mel.eval('polySelectBorderShell 1')
	uvBorder = cmds.polyListComponentConversion(te = True, internal = True)
	uvBorder = cmds.ls( uvBorder, fl = True )

	for edge in uvBorder:
		edgeUVs = cmds.polyListComponentConversion(edge, tuv = True)
		edgeUVs = cmds.ls( edgeUVs, fl = True )
		if(len(edgeUVs) > 2):
			finalBorder.append(edge)

	#Edge conversion and cut
	cutEdges = cmds.polyListComponentConversion(finalBorder, te = True)
	cmds.polySplitEdge(cutEdges)
