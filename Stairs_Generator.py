import maya.cmds as cmds
import math


# WinName = "Stairs_Generator"

# if cmds.window(WinName, q=True, ex=True):
# 	cmds.deleteUI(WinName)

# WinWidth = 400
# WinForm = cmds.window(WinName, t='Stairs_Generator', mxb=True, mnb=True, s=True, wh=[WinWidth,300], resizeToFitChildren=True)


# cmds.columnLayout( adjustableColumn=True )
# St_width_Slider = cmds.floatSliderGrp( label='Width', field=True, minValue=1, maxValue=10, value=1, cc='Width_Change_Value()')



# cmds.showWindow(WinName)


### INITIAL VALUE ###


Floor_count = 20


St_count = 7
St_width = 1
St_depth = 4
St_height = 0.5
St_dilength = abs(math.sqrt(St_width**2 + St_height**2))


Fence_angle = math.degrees(math.atan(St_height/St_width))
Fence_height = 0.1
Fence_depth = 0.2


M_Pole_Count = 2
M_Pole_Side_Count = 4


Pl_radius = 0.05
Pl_height = 2


Gap = 0.3
Pole_Step_Gap = St_depth/2-Gap


St_M_width = St_width*5
St_M_depth = St_depth
St_M_height = St_height


#-----------------------------Floor Count----------------------------------


def StairCase_Floor():

	for Fl_cnt in range(1, Floor_count+1):

		StairCase_Unit(Fl_cnt)

		cmds.xform('Staircase_f{0}'.format(Fl_cnt), centerPivots=True)

		if Fl_cnt == 1:

			cmds.move(0, 0, 0, 'Staircase_f{0}'.format(Fl_cnt), ws=True)

		elif Fl_cnt % 2 == 0 and Fl_cnt != 1:

			cmds.setAttr('Staircase_f{0}.rotateY'.format(Fl_cnt), 180)
			cmds.move(0, St_height*(St_count+1)*(Fl_cnt-1), -St_depth, 'Staircase_f{0}'.format(Fl_cnt), ws=True)


		elif Fl_cnt % 2 != 0 and Fl_cnt != 1:

			cmds.move(0, St_height*(St_count+1)*(Fl_cnt-1), 0, 'Staircase_f{0}'.format(Fl_cnt), ws=True)

	cmds.select(all=True)
	cmds.makeIdentity(apply=True)



def StairCase_Unit(Fl_cnt):


	for Fl_num in range(Fl_cnt, Fl_cnt+1):

		cmds.group(name='Staircase_f{0}'.format(Fl_num), empty=True)
		cmds.group(name='Mid_f{0}_Pole_Grp'.format(Fl_num), empty=True)

	# First Floor

		if Fl_num == 1:
	
		#-----------------------------Stair Step----------------------------------

			Stair_Grp = cmds.group(name='Stair_Step_f{0}'.format(Fl_num), empty=True)

			
			for cnt in range(St_count):

				if cnt == 0:

					# Step_Obj_Cube

					StairCube = cmds.polyCube(name='Stair_f{0}_{1}'.format(Fl_num, cnt+1), w=St_width, h=St_height, d=St_depth, ch=True)


					cmds.move(St_width*cnt, St_height*cnt, 0)
					cmds.rename("polyCube1", "St_f{0}_polyCube{1}".format(Fl_num, 1))

				else:

					# Step_Obj_Cube

					StairCube = cmds.polyCube(name='Stair_f{0}_{1}'.format(Fl_num, cnt+1), w=St_width, h=St_height, d=St_depth, ch=True)



					cmds.move(St_width*cnt, St_height*cnt, 0)
					cmds.connectAttr('St_f{0}_polyCube{1}.width'.format(Fl_num, 1), 'polyCube{0}.width'.format(1))
					cmds.connectAttr('St_f{0}_polyCube{1}.height'.format(Fl_num, 1), 'polyCube{0}.height'.format(1))
					cmds.connectAttr('St_f{0}_polyCube{1}.depth'.format(Fl_num, 1), 'polyCube{0}.depth'.format(1))
					cmds.rename('polyCube1', 'St_f{0}_polyCube{1}'.format(Fl_num, cnt+1))


				cmds.parent('Stair_f{0}_{1}'.format(Fl_num, cnt+1), 'Stair_Step_f{0}'.format(Fl_num), r=True)

			cmds.parent('Stair_Step_f{0}'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Stair Right Pole----------------------------------


			R_Pole_Grp = cmds.group(name='R_f{0}_Pole_Grp'.format(Fl_num), empty=True)


			for cnt in range(St_count+1):

				if cnt == 0:
					StairPole = cmds.polyCylinder(name='R_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*cnt, (St_height)*cnt + Pl_height/2 + St_height/2, Pole_Step_Gap)
					cmds.rename("polyCylinder1", "R_f{0}_polyCylinder{1}".format(Fl_num, 1))

				else:
					StairPole = cmds.polyCylinder(name='R_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*cnt, (St_height)*cnt + Pl_height/2 + St_height/2, Pole_Step_Gap, r=True)
					cmds.connectAttr('R_f{0}_polyCylinder{1}.radius'.format(Fl_num, 1), 'polyCylinder{0}.radius'.format(1))
					cmds.connectAttr('R_f{0}_polyCylinder{1}.height'.format(Fl_num, 1), 'polyCylinder{0}.height'.format(1))
					cmds.rename("polyCylinder1", "R_f{0}_polyCylinder{1}".format(Fl_num, cnt+1))


				cmds.parent('R_f{0}_Pole{1}'.format(Fl_num, cnt+1), 'R_f{0}_Pole_Grp'.format(Fl_num), r=True)

			cmds.parent('R_f{0}_Pole_Grp'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Stair Left Pole----------------------------------

			L_Pole_Grp = cmds.group(name='L_f{0}_Pole_Grp'.format(Fl_num), empty=True)


			for cnt in range(St_count+1):

				if cnt == 0:
					StairPole = cmds.polyCylinder(name='L_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*cnt, (St_height)*cnt + Pl_height/2 + St_height/2, -Pole_Step_Gap)
					cmds.rename("polyCylinder1", "L_f{0}_polyCylinder{1}".format(Fl_num, 1))

				else:
					StairPole = cmds.polyCylinder(name='L_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*cnt, (St_height)*cnt + Pl_height/2 + St_height/2, -Pole_Step_Gap, r=True)
					cmds.connectAttr('L_f{0}_polyCylinder{1}.radius'.format(Fl_num, 1), 'polyCylinder{0}.radius'.format(1))
					cmds.connectAttr('L_f{0}_polyCylinder{1}.height'.format(Fl_num, 1), 'polyCylinder{0}.height'.format(1))
					cmds.rename("polyCylinder1", "L_f{0}_polyCylinder{1}".format(Fl_num, cnt+1))


				cmds.parent('L_f{0}_Pole{1}'.format(Fl_num, cnt+1), 'L_f{0}_Pole_Grp'.format(Fl_num), r=True)

			cmds.parent('L_f{0}_Pole_Grp'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Middle Stair----------------------------------

			for cnt in range(Fl_cnt, Fl_cnt+1):

			# UP_Mid_Stair
				cmds.polyCube(name='Mid_f{0}_Stair{1}'.format(Fl_num, cnt), w=St_width*5, h=St_height, d=St_depth, ch=True)
				cmds.rename('polyCube1', 'St_M_f{0}_polyCube{1}'.format(Fl_num, cnt))
				cmds.move((St_count-1)*St_width+(St_M_width+St_width)/2, St_count*St_height, 0)

				cmds.parent('Mid_f{0}_Stair{1}'.format(Fl_num, cnt), 'Staircase_f{0}'.format(Fl_num), r=True)
	
		#-----------------------------Right fence----------------------------------


			cmds.polyCube(name='R_f{0}_fence{1}'.format(Fl_num, 1), w=St_dilength*(St_count+0.2), h=Fence_height, d=Fence_depth, ch=True)
			cmds.rename('polyCube1', 'R_f{0}_Fe_polyCube{1}'.format(Fl_num, 1))
			
			cmds.move(St_width*St_count/2, St_height*(St_count)/2+Pl_height, Pole_Step_Gap)
			cmds.rotate(0, 0, Fence_angle)
			cmds.move(St_dilength/2, 0, 0, r=True, objectSpace=True)
			

			cmds.parent('R_f{0}_fence{1}'.format(Fl_num, 1), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Left fence----------------------------------


			cmds.polyCube(name='L_f{0}_fence{1}'.format(Fl_num, 1), w=St_dilength*(St_count+0.5), h=Fence_height, d=Fence_depth, ch=True)
			cmds.rename('polyCube1', 'L_f{0}_Fe_polyCube{1}'.format(Fl_num, 1))
			
			cmds.move(St_width*St_count/2, St_height*(St_count)/2+Pl_height, -Pole_Step_Gap)
			cmds.rotate(0, 0, Fence_angle)
			cmds.move(St_dilength/2, 0, 0, r=True, objectSpace=True)
			

			cmds.parent('L_f{0}_fence{1}'.format(Fl_num, 1), 'Staircase_f{0}'.format(Fl_num), r=True)
			
	# Next Floor

		else:

		#-----------------------------Stair Step----------------------------------

			Stair_Grp = cmds.group(name='Stair_Step_f{0}'.format(Fl_num), empty=True)

			
			for cnt in range(St_count):

				if cnt == 0:

					# Step_Obj_Cube

					StairCube = cmds.polyCube(name='Stair_f{0}_{1}'.format(Fl_num, cnt+1), w=St_width, h=St_height, d=St_depth, ch=True)

					cmds.move(St_width*cnt, St_height*cnt, 0)
					cmds.rename("polyCube1", "St_f{0}_polyCube{1}".format(Fl_num, 1))

				else:

					# Step_Obj_Cube

					StairCube = cmds.polyCube(name='Stair_f{0}_{1}'.format(Fl_num, cnt+1), w=St_width, h=St_height, d=St_depth, ch=True)

					cmds.move(St_width*cnt, St_height*cnt, 0)
					cmds.connectAttr('St_f{0}_polyCube{1}.width'.format(Fl_num, 1), 'polyCube{0}.width'.format(1))
					cmds.connectAttr('St_f{0}_polyCube{1}.height'.format(Fl_num, 1), 'polyCube{0}.height'.format(1))
					cmds.connectAttr('St_f{0}_polyCube{1}.depth'.format(Fl_num, 1), 'polyCube{0}.depth'.format(1))
					cmds.rename('polyCube1', 'St_f{0}_polyCube{1}'.format(Fl_num, cnt+1))


				cmds.parent('Stair_f{0}_{1}'.format(Fl_num, cnt+1), 'Stair_Step_f{0}'.format(Fl_num), r=True)

			cmds.parent('Stair_Step_f{0}'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Stair Right Pole----------------------------------


			R_Pole_Grp = cmds.group(name='R_f{0}_Pole_Grp'.format(Fl_num), empty=True)


			for cnt in range(St_count+2):

				if cnt == 0:
					StairPole = cmds.polyCylinder(name='R_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*(cnt-1), (St_height)*(cnt-1) + Pl_height/2 + St_height/2, Pole_Step_Gap)
					cmds.rename("polyCylinder1", "R_f{0}_polyCylinder{1}".format(Fl_num, 1))

				else:
					StairPole = cmds.polyCylinder(name='R_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*(cnt-1), (St_height)*(cnt-1) + Pl_height/2 + St_height/2, Pole_Step_Gap, r=True)
					cmds.connectAttr('R_f{0}_polyCylinder{1}.radius'.format(Fl_num, 1), 'polyCylinder{0}.radius'.format(1))
					cmds.connectAttr('R_f{0}_polyCylinder{1}.height'.format(Fl_num, 1), 'polyCylinder{0}.height'.format(1))
					cmds.rename("polyCylinder1", "R_f{0}_polyCylinder{1}".format(Fl_num, cnt+1))

				cmds.parent('R_f{0}_Pole{1}'.format(Fl_num, cnt+1), 'R_f{0}_Pole_Grp'.format(Fl_num), r=True)
			cmds.parent('R_f{0}_Pole_Grp'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Stair Left Pole----------------------------------

			L_Pole_Grp = cmds.group(name='L_f{0}_Pole_Grp'.format(Fl_num), empty=True)


			for cnt in range(St_count+2):

				if cnt == 0:
					StairPole = cmds.polyCylinder(name='L_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*(cnt-1), (St_height)*(cnt-1) + Pl_height/2 + St_height/2, -Pole_Step_Gap)
					cmds.rename("polyCylinder1", "L_f{0}_polyCylinder{1}".format(Fl_num, 1))

				else:
					StairPole = cmds.polyCylinder(name='L_f{0}_Pole{1}'.format(Fl_num, cnt+1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.move(St_width*(cnt-1), (St_height)*(cnt-1) + Pl_height/2 + St_height/2, -Pole_Step_Gap, r=True)
					cmds.connectAttr('L_f{0}_polyCylinder{1}.radius'.format(Fl_num, 1), 'polyCylinder{0}.radius'.format(1))
					cmds.connectAttr('L_f{0}_polyCylinder{1}.height'.format(Fl_num, 1), 'polyCylinder{0}.height'.format(1))
					cmds.rename("polyCylinder1", "L_f{0}_polyCylinder{1}".format(Fl_num, cnt+1))


				cmds.parent('L_f{0}_Pole{1}'.format(Fl_num, cnt+1), 'L_f{0}_Pole_Grp'.format(Fl_num), r=True)

			cmds.parent('L_f{0}_Pole_Grp'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Middle Stair----------------------------------

			for cnt in range(Fl_cnt, Fl_cnt+1):

			# UP_Mid_Stair
				cmds.polyCube(name='Mid_f{0}_Stair{1}'.format(Fl_num, 1), w=St_width*5, h=St_height, d=St_depth, ch=True)
				cmds.rename('polyCube1', 'St_M_f{0}_polyCube{1}'.format(Fl_num, cnt-1))
				cmds.move((St_count-1)*St_width+(St_M_width+St_width)/2, St_count*St_height, 0)
				
			# DOWN_Mid_Stair
				cmds.polyCube(name='Mid_f{0}_Stair{1}'.format(Fl_num-1, 2), w=St_width*5, h=St_height, d=St_depth, ch=True)
				cmds.rename('polyCube1', 'St_M_f{0}_polyCube{1}'.format(Fl_num-1, cnt-1))
				cmds.move(-(St_M_width+St_width)/2, -St_height, 0)

				cmds.parent('Mid_f{0}_Stair{1}'.format(Fl_num, 1), 'Staircase_f{0}'.format(Fl_num), r=True)
				cmds.parent('Mid_f{0}_Stair{1}'.format(Fl_num-1, 2), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Right fence----------------------------------

			cmds.polyCube(name='R_f{0}_fence{1}'.format(Fl_num, 1), w=St_dilength*(St_count+1), h=Fence_height, d=Fence_depth, ch=True)
			cmds.rename('polyCube1', 'R_f{0}_Fe_polyCube{1}'.format(Fl_num, 1))
			
			cmds.move(St_width*St_count/2, St_height*(St_count)/2+Pl_height, Pole_Step_Gap, 'R_f{0}_fence{1}'.format(Fl_num, 1))
			cmds.rotate(0, 0, Fence_angle)
			# cmds.move(-St_dilength/2, 0, 0, 'R_f{0}_fence{1}'.format(Fl_num, 1), r=True, objectSpace=True, worldSpaceDistance=True)

			cmds.parent('R_f{0}_fence{1}'.format(Fl_num, 1), 'Staircase_f{0}'.format(Fl_num), r=True)

		#-----------------------------Left fence----------------------------------

			cmds.polyCube(name='L_f{0}_fence{1}'.format(Fl_num, 1), w=St_dilength*(St_count+1.3), h=Fence_height, d=Fence_depth, ch=True)
			cmds.rename('polyCube1', 'L_f{0}_Fe_polyCube{1}'.format(Fl_num, 1))
			
			cmds.move(St_width*St_count/2, St_height*(St_count)/2+Pl_height, -Pole_Step_Gap, 'L_f{0}_fence{1}'.format(Fl_num, 1))
			cmds.rotate(0, 0, Fence_angle)
			# cmds.move(-St_dilength/2, 0, 0, 'L_f{0}_fence{1}'.format(Fl_num, 1), r=True, objectSpace=True, worldSpaceDistance=True)

			cmds.parent('L_f{0}_fence{1}'.format(Fl_num, 1), 'Staircase_f{0}'.format(Fl_num), r=True)

			

		cmds.parent('Mid_f{0}_Pole_Grp'.format(Fl_num), 'Staircase_f{0}'.format(Fl_num), r=True)


def Mid_Pole_Standard():

	for Fl_num in range(1, Floor_count+1):

		if Fl_num == 1:

			for cnt in range(1,2):

				cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
				cmds.rename('polyCylinder1', 'Mid_f{0}_polyCylinder{1}'.format(Fl_num, cnt))

				Get_Pos1 = cmds.pointPosition('Mid_f{0}_Stair{1}.vtx[{2}]'.format(Fl_num, 1, 3))				

				cmds.move(Get_Pos1[0]-Gap, Get_Pos1[1]+Pl_height/2, Get_Pos1[2]-Gap, 'Mid_f{0}_Pole{1}'.format(Fl_num, cnt), ws=True)

				cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt), 'Mid_f{0}_Pole_Grp'.format(Fl_num), r=True)

		else:

			if Fl_num % 2 == 0:

			# Down
				for cnt in range(1):

					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num-1, 2), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.rename('polyCylinder1', 'Mid_f{0}_polyCylinder{1}'.format(Fl_num-1, 2))

					Get_Pos2 = cmds.pointPosition('Mid_f{0}_Stair{1}.vtx[{2}]'.format(Fl_num-1, 2, 2))

					cmds.move(Get_Pos2[0]-Gap, Get_Pos2[1]+Pl_height/2, Get_Pos2[2]+Gap, 'Mid_f{0}_Pole{1}'.format(Fl_num-1, 2), ws=True)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num-1, 2), 'Mid_f{0}_Pole_Grp'.format(Fl_num-1), r=True)

			# UP
				for cnt in range(1):

					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, 1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.rename('polyCylinder1', 'Mid_f{0}_polyCylinder{1}'.format(Fl_num, 1))

					Get_Pos3 = cmds.pointPosition('Mid_f{0}_Stair{1}.vtx[{2}]'.format(Fl_num, 1, 3))

					cmds.move(Get_Pos3[0]+Gap, Get_Pos3[1]+Pl_height/2, Get_Pos3[2]+Gap, 'Mid_f{0}_Pole{1}'.format(Fl_num, 1), ws=True)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, 1), 'Mid_f{0}_Pole_Grp'.format(Fl_num), r=True)


			elif Fl_num % 2 != 0:

			# Down
				for cnt in range(1):

					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num-1, 2), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.rename('polyCylinder1', 'Mid_f{0}_polyCylinder{1}'.format(Fl_num-1, 2))

					Get_Pos2 = cmds.pointPosition('Mid_f{0}_Stair{1}.vtx[{2}]'.format(Fl_num-1, 2, 2))

					cmds.move(Get_Pos2[0]+Gap, Get_Pos2[1]+Pl_height/2, Get_Pos2[2]-Gap, 'Mid_f{0}_Pole{1}'.format(Fl_num-1, 2), ws=True)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num-1, 2), 'Mid_f{0}_Pole_Grp'.format(Fl_num-1), r=True)

			# UP
				for cnt in range(1):

					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, 1), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)
					cmds.rename('polyCylinder1', 'Mid_f{0}_polyCylinder{1}'.format(Fl_num, 1))

					Get_Pos3 = cmds.pointPosition('Mid_f{0}_Stair{1}.vtx[{2}]'.format(Fl_num, 1, 3))

					cmds.move(Get_Pos3[0]-Gap, Get_Pos3[1]+Pl_height/2, Get_Pos3[2]-Gap, 'Mid_f{0}_Pole{1}'.format(Fl_num, 1), ws=True)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, 1), 'Mid_f{0}_Pole_Grp'.format(Fl_num), r=True)


def Mid_Pole():

	for Fl_num in range(1, Floor_count):

		if Fl_num == 1:

			for cnt in range(M_Pole_Count):

				Pole_posX1 = Get_St_Pole_Position(Fl_num, St_count+1)[0]
				Pole_posX2 = Get_St_Pole_Position(Fl_num+1, 1)[0]
				Pole_posX3 = Get_Mid_Pole_Position(Fl_num, 1)[0]
				Pole_posX4 = Get_Mid_Pole_Position(Fl_num, 2)[0]
				

				Pole_posY1 = Get_St_Pole_Position(Fl_num, St_count+1)[1]
				Pole_posY2 = Get_St_Pole_Position(Fl_num+1, 1)[1]
				Pole_posY3 = Get_Mid_Pole_Position(Fl_num, 1)[1]
				Pole_posY4 = Get_Mid_Pole_Position(Fl_num, 2)[1]

				Pole_posZ1 = Get_St_Pole_Position(Fl_num, St_count+1)[2]
				Pole_posZ2 = Get_St_Pole_Position(Fl_num+1, 1)[2]
				Pole_posZ3 = Get_Mid_Pole_Position(Fl_num, 1)[2]
				Pole_posZ4 = Get_Mid_Pole_Position(Fl_num, 2)[2]

				cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

				Pole_distance1 = abs(Pole_posX1 - Pole_posX3)/(M_Pole_Count+1)

				cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3), Pole_posX1+(Pole_distance1*(cnt+1)))
				cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3), Pole_posY1+(Pl_height/2))
				cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3), Pole_posZ1)

				cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3), 'Mid_f{0}_Pole_Grp'.format(Fl_num))


				cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

				Pole_distance2 = abs(Pole_posX2 - Pole_posX4)/(M_Pole_Count+1)

				cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posX2+(Pole_distance2*(cnt+1)))
				cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posY2+(Pl_height/2))
				cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posZ2)

				cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count), 'Mid_f{0}_Pole_Grp'.format(Fl_num))

		else:

			if Fl_num % 2 == 0:

				for cnt in range(M_Pole_Count):

					Pole_posX1 = Get_St_Pole_Position(Fl_num, St_count+2)[0]
					Pole_posX2 = Get_St_Pole_Position(Fl_num+1, 1)[0]
					Pole_posX3 = Get_Mid_Pole_Position(Fl_num, 1)[0]
					Pole_posX4 = Get_Mid_Pole_Position(Fl_num, 2)[0]

					Pole_posY1 = Get_St_Pole_Position(Fl_num, St_count+2)[1]
					Pole_posY2 = Get_St_Pole_Position(Fl_num+1, 1)[1]
					Pole_posY3 = Get_Mid_Pole_Position(Fl_num, 1)[1]
					Pole_posY4 = Get_Mid_Pole_Position(Fl_num, 2)[1]

					Pole_posZ1 = Get_St_Pole_Position(Fl_num, St_count+2)[2]
					Pole_posZ2 = Get_St_Pole_Position(Fl_num+1, 1)[2]
					Pole_posZ3 = Get_Mid_Pole_Position(Fl_num, 1)[2]
					Pole_posZ4 = Get_Mid_Pole_Position(Fl_num, 2)[2]

					Pole_distance1 = abs(Pole_posX1 - Pole_posX3)/(M_Pole_Count+1)
					Pole_distance2 = abs(Pole_posX2 - Pole_posX4)/(M_Pole_Count+1)

					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

					cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3), Pole_posX1-(Pole_distance1*(cnt+1)))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3), Pole_posY1+(Pl_height/2))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3), Pole_posZ1)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3), 'Mid_f{0}_Pole_Grp'.format(Fl_num))


					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

					cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posX2-(Pole_distance2*(cnt+1)))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posY4+(Pl_height/2))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posZ4)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count), 'Mid_f{0}_Pole_Grp'.format(Fl_num))


			elif Fl_num % 2 != 0:

				for cnt in range(M_Pole_Count):

					Pole_posX1 = Get_St_Pole_Position(Fl_num, St_count+2)[0]
					Pole_posX2 = Get_St_Pole_Position(Fl_num+1, 1)[0]
					Pole_posX3 = Get_Mid_Pole_Position(Fl_num, 1)[0]
					Pole_posX4 = Get_Mid_Pole_Position(Fl_num, 2)[0]

					Pole_posY1 = Get_St_Pole_Position(Fl_num, St_count+2)[1]
					Pole_posY2 = Get_St_Pole_Position(Fl_num+1, 1)[1]
					Pole_posY3 = Get_Mid_Pole_Position(Fl_num, 1)[1]
					Pole_posY4 = Get_Mid_Pole_Position(Fl_num, 2)[1]

					Pole_posZ1 = Get_St_Pole_Position(Fl_num, St_count+2)[2]
					Pole_posZ2 = Get_St_Pole_Position(Fl_num+1, 1)[2]
					Pole_posZ3 = Get_Mid_Pole_Position(Fl_num, 1)[2]
					Pole_posZ4 = Get_Mid_Pole_Position(Fl_num, 2)[2]

					Pole_distance1 = abs(Pole_posX1 - Pole_posX3)/(M_Pole_Count+1)
					Pole_distance2 = abs(Pole_posX2 - Pole_posX4)/(M_Pole_Count+1)

					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

					cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3), Pole_posX1+(Pole_distance1*(cnt+1)))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3), Pole_posY1+(Pl_height/2))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3), Pole_posZ1)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3), 'Mid_f{0}_Pole_Grp'.format(Fl_num))


					cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

					cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posX2+(Pole_distance2*(cnt+1)))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posY2+(Pl_height/2))
					cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3+M_Pole_Count), Pole_posZ2)

					cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count), 'Mid_f{0}_Pole_Grp'.format(Fl_num))


	for Fl_num in range(1, Floor_count):

		if Fl_num % 2 == 0:

			for cnt in range(M_Pole_Side_Count):

				Pole_Side_posX1 = Get_Mid_Pole_Position(Fl_num, 1)[0]
				
				Pole_Side_posY1 = Get_Mid_Pole_Position(Fl_num, 1)[1]

				Pole_Side_posZ1 = Get_Mid_Pole_Position(Fl_num, 1)[2]
				Pole_Side_posZ2 = Get_Mid_Pole_Position(Fl_num, 2)[2]

				cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

				Get_Side_distance = abs(Pole_Side_posZ1-Pole_Side_posZ2)/(M_Pole_Side_Count+1)

				cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), Pole_Side_posX1)
				cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), Pole_Side_posY1+(Pl_height/2))
				cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), Pole_Side_posZ1+(Get_Side_distance*(cnt+1)))

				cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), 'Mid_f{0}_Pole_Grp'.format(Fl_num))

		elif Fl_num % 2 != 0:

			for cnt in range(M_Pole_Side_Count):

				Pole_Side_posX1 = Get_Mid_Pole_Position(Fl_num, 1)[0]
				
				Pole_Side_posY1 = Get_Mid_Pole_Position(Fl_num, 1)[1]

				Pole_Side_posZ1 = Get_Mid_Pole_Position(Fl_num, 1)[2]
				Pole_Side_posZ2 = Get_Mid_Pole_Position(Fl_num, 2)[2]

				cmds.polyCylinder(name='Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), radius=Pl_radius, height=Pl_height, sx=8, sz=1, ch=True)

				Get_Side_distance = abs(Pole_Side_posZ1-Pole_Side_posZ2)/(M_Pole_Side_Count+1)

				cmds.setAttr('Mid_f{0}_Pole{1}.translateX'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), Pole_Side_posX1)
				cmds.setAttr('Mid_f{0}_Pole{1}.translateY'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), Pole_Side_posY1+(Pl_height/2))
				cmds.setAttr('Mid_f{0}_Pole{1}.translateZ'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), Pole_Side_posZ1-(Get_Side_distance*(cnt+1)))

				cmds.parent('Mid_f{0}_Pole{1}'.format(Fl_num, cnt+3+M_Pole_Count+M_Pole_Side_Count), 'Mid_f{0}_Pole_Grp'.format(Fl_num))


def Mid_Fence():

	

	for Fl_num in range(1, Floor_count):

		Pole_Side_posX1 = Get_Mid_Pole_Position(Fl_num, 1)[0]
		Pole_posX1 = Get_St_Pole_Position(Fl_num+1, 1)[0]
		Pole_posX2 = Get_Mid_Pole_Position(Fl_num, 2)[0]


		Pole_Side_posY1 = Get_Mid_Pole_Position(Fl_num, 1)[1]

		Pole_Side_posZ1 = Get_Mid_Pole_Position(Fl_num, 1)[2]
		Pole_Side_posZ2 = Get_Mid_Pole_Position(Fl_num, 2)[2]

		Pole_distance = abs(Pole_posX1-Pole_posX2)
		Pole_Side_distance = abs(Pole_Side_posZ1-Pole_Side_posZ2)
		Pole_Side_pos_Center = abs(Pole_Side_posZ1-Pole_Side_posZ2)/2

		cmds.polyCube(name='R_f{0}_Mid_fence{1}'.format(Fl_num, 1), w=Pole_Side_distance+Fence_depth, h=Fence_height, d=Fence_depth, ch=True)
		cmds.rename('polyCube1', 'R_f{0}_Mid_Fe_polyCube{1}'.format(Fl_num, 1))
		
		cmds.rotate(0, 90, 0)
		

		if Fl_num % 2 == 0:
			cmds.move(Pole_Side_posX1, Pole_Side_posY1+Pl_height, Pole_Side_posZ1+Pole_Side_pos_Center)

			cmds.polyConnectComponents('R_f{0}_Mid_fence{1}.e[0:3]'.format(Fl_num, 1), adjustEdgeFlow=1, insertWithEdgeFlow=0, ch=1)
			cmds.polyConnectComponents('R_f{0}_Mid_fence{1}.e[12:15]'.format(Fl_num, 1), adjustEdgeFlow=1, insertWithEdgeFlow=0, ch=1)

			cmds.move(0, 0, St_M_depth-Gap-Fence_depth/2, 'R_f{0}_Mid_fence{1}.e[16:19]'.format(Fl_num, 1), r=True)			
			cmds.move(0, 0, -St_M_depth/2+Gap, 'R_f{0}_Mid_fence{1}.e[24:27]'.format(Fl_num, 1), r=True)

			cmds.polyExtrudeFacet('R_f{0}_Mid_fence{1}.f[0]'.format(Fl_num, 1), constructionHistory=1, keepFacesTogether=1, divisions=1, twist=0, taper=1, off=0, thickness=Pole_distance-Fence_depth/2, smoothingAngle=30)
			cmds.polyExtrudeFacet('R_f{0}_Mid_fence{1}.f[10]'.format(Fl_num, 1), constructionHistory=1, keepFacesTogether=1, divisions=1, twist=0, taper=1, off=0, thickness=Pole_distance-Fence_depth/2, smoothingAngle=30)


		else:
			cmds.move(Pole_Side_posX1, Pole_Side_posY1+Pl_height, Pole_Side_posZ2+Pole_Side_pos_Center)

			cmds.polyConnectComponents('R_f{0}_Mid_fence{1}.e[0:3]'.format(Fl_num, 1), adjustEdgeFlow=1, insertWithEdgeFlow=0, ch=1)
			cmds.polyConnectComponents('R_f{0}_Mid_fence{1}.e[12:15]'.format(Fl_num, 1), adjustEdgeFlow=1, insertWithEdgeFlow=0, ch=1)

			cmds.move(0, 0, St_M_depth-Gap-Fence_depth/2, 'R_f{0}_Mid_fence{1}.e[16:19]'.format(Fl_num, 1), r=True)			
			cmds.move(0, 0, -St_M_depth/2+Gap, 'R_f{0}_Mid_fence{1}.e[24:27]'.format(Fl_num, 1), r=True)

			cmds.polyExtrudeFacet('R_f{0}_Mid_fence{1}.f[2]'.format(Fl_num, 1), constructionHistory=1, keepFacesTogether=1, divisions=1, twist=0, taper=1, off=0, thickness=Pole_distance-Fence_depth/2, smoothingAngle=30)
			cmds.polyExtrudeFacet('R_f{0}_Mid_fence{1}.f[12]'.format(Fl_num, 1), constructionHistory=1, keepFacesTogether=1, divisions=1, twist=0, taper=1, off=0, thickness=Pole_distance-Fence_depth/2, smoothingAngle=30)

		
		cmds.parent('R_f{0}_Mid_fence{1}'.format(Fl_num, 1), 'Staircase_f{0}'.format(Fl_num), r=True)


def Get_St_Pole_Position(Fl_cnt, cnt):

	A = cmds.pointPosition('R_f{0}_Pole{1}.vtx[{2}]'.format(Fl_cnt, cnt, 16), w=True)

	return A
	
def Get_Mid_Pole_Position(Fl_cnt, cnt):

	A = cmds.pointPosition('Mid_f{0}_Pole{1}.vtx[{2}]'.format(Fl_cnt, cnt, 16), w=True)

	return A


StairCase_Floor()
Mid_Pole_Standard()
Mid_Pole()
Mid_Fence()


SC_GRP = cmds.group(name='StairCase_GEO', empty=True)

for floor in range(1, Floor_count+1):
	
	cmds.parent('Staircase_f{0}'.format(floor), 'StairCase_GEO')

cmds.select(all=True)
cmds.delete(ch=True)