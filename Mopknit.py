## MOPKNIT ##



import maya.cmds as cmds
import maya.mel as mel
import math


class MOPKNIT:





	def mopKnit():
		Origin = 0
		Facing = "Z"
		autoScale = 1
		Scale = 100.0

		if ( cmds.optionVar(ex = "mopKnitOrigin")):
			Origin = cmds.optionVar(q = "mopKnitOrigin")

		if ( cmds.optionVar(ex = "mopKnitFacing")):
			Origin = cmds.optionVar(q = "mopKnitFacing")

		if ( cmds.optionVar(ex = "mopKnitAutoScale")):
			Origin = cmds.optionVar(q = "mopKnitAutoScale")

		if ( cmds.optionVar(ex = "mopKnitScale")):
			Origin = cmds.optionVar(q = "mopKnitScale")

		if (autoScale == 1):
			Scale = 0

		## Get the current tool, swap to Select to minimise warnings.

		Context = cmds.currentCtx()
		global gSelect
		cmds.setToolTo(gSelect)

		## Check selections.
		Sel = cmds.ls(sl = True, tr = True)
		if(len(Sel) == 0):
			Sel = cmds.ls(hl = True)
			cmds.warning("Please select at least one object")
			return

		for obj in Sel:
			if():
				cmds.warning("This is not a valid mesh.")

			else:
				dup = cmds.duplicate(obj, name="mopKnit_Source")
				knitMeshOrig = dup[0]
				delete(knitMeshOrig, ch=True)
				splitMeshUVs(knitMeshOrig)
				delete(knitMeshOrig, ch=True)

				#Copy mesh again, unfold to UV layout

				dup = cmds.duplicate(knitMeshOrig, name="( 'mopKnit_' + obj )")
				str(knitMesh) = dup[0]
				UVToMesh(knitMesh, Origin, Facing, Scale)
				delete("knitMesh", ch=True)

				#Connect the original shape up to the final transform

				knitMeshOrigShapes = cmds.listRelatives("knitMeshOrig", f=True, s=True, ni=True)
				knitMeshShapes = cmds.listRelatives("knitMesh", f=True, s=True, ni=True)
				cmds.parent(knitMeshOrigShapes[0], knitMesh, r=True, s=True)

				#Remove original transform, now empty

				cmds.delete(knitMeshOrig)
				knitMeshOrigShapes = cmds.listRelatives(knitMeshOrig, f=True, s=True, ni=True)
#			    knitMeshOrigShapes = mel.eval('stringArrayRemove("knitMeshShapes", "knitMeshOrigShapes")')

				#Create blendShape

				cmds.blendShape(knitMeshOrigShapes[0], knitMeshShapes[0], name = "mopKnit_blendShape")
				cmds.setAttr((knitMeshOrigShapes[0] + ".intermediateObject"), 1)
				cmds.showHidden(knitMesh)

		cmds.select(Sel, r=True)
		cmds.setToolTo(context)

		def findShapes(obj):
			shapes = cmds.listRelatives(obj, f = True, s = True, ni = True)
			found = 0
			for shape in shapes:
				if cmds.nodeType(shape) == "mesh":
					found = 1

			return found


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


		def UVToMesh(obj, Origin, Facing, Scale):


			bounds = cmds.polyEvaluate(obj, boundingBox = True)

			# If scale is 0, calculated scale factor from object area.
			if(Scale == 0):
				Area = cmds.polyEvaluate(obj, area = True)
				Scale = math.sqrt(Area)

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
						bounds[2][0])) # Offset.

				cmds.progressWindow(edit=True, progress=i)

				i += 1

			cmds.progressWindow(endProgress=True)

MOPKNIT()