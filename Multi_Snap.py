### Multi_Snap ###

### Made by HyunWoo /// ver.001 ###

#--------------- Caution -----------------#

#The number of object name is same (Source and Target)#

#Example

# Source object name ==>  My_shpere_1, My_shpere_2, My_shpere_3
# Target object name ==>  Cone_1, Cone_2, Cone_3
 
# Last number have to same number






import maya.cmds as cmds
import maya.mel as mel
from functools import partial

# Window

WinName = "Multi_Snap"

if cmds.window(WinName, q=True, ex=True):
    cmds.deleteUI(WinName)

WinWidth = 400
WinFrom = cmds.window(WinName, t='Multi_Snap_Tool', mxb=True, mnb=True, s=True, wh=[WinWidth,300], resizeToFitChildren=True)

# Layout

MainForm = cmds.formLayout(vis=True, numberOfDivisions=100)

Main_Column = cmds.columnLayout(width=WinWidth)

MainRL_Width = [WinWidth*0.5, WinWidth*0.5]
MainRow = cmds.rowLayout(width=WinWidth, numberOfColumns = 2, vis=True, columnWidth2=MainRL_Width)


Fst_Column = cmds.columnLayout(width=MainRL_Width[0])

tmpRowWidth=[MainRL_Width[0]*0.5, MainRL_Width[0]*0.5]

cmds. rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
Src_Text = cmds.text(l='Source', width=tmpRowWidth[0], height=15, align='center')
Tar_Text = cmds.text(l='Target', width=tmpRowWidth[1], height=15, align='center')
cmds.setParent('..')


cmds. rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
Src_TSL = cmds.textScrollList('Src_List', width=tmpRowWidth[0], nr=8, ams=True)
Tar_TSL = cmds.textScrollList('Tar_List', width=tmpRowWidth[1], nr=8, ams=True)
cmds.setParent('..')


cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
SrcListUpdateB = cmds.button('MS_SrcUpdateB', w=tmpRowWidth[0], l='Update', c='updateSrcList()')
TarListUpdateB = cmds.button('MS_TarUpdateB', w=tmpRowWidth[1], l='Update', c='updateTarList()')
cmds.setParent('..')


cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
SrcListAppendB = cmds.button('MS_SrcAppendB', w=tmpRowWidth[0], l='Append', c='appendSrcList()')
TarListAppendB = cmds.button('MS_TarAppendB', w=tmpRowWidth[1], l='Append', c='appendTarList()')
cmds.setParent('..')


cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
SrcListClearB = cmds.button('MS_SrcClearB', w=tmpRowWidth[0], l='Clear', c='clearSrcList()')
TarListClearB = cmds.button('MS_TarClearB', w=tmpRowWidth[1], l='Clear', c='clearTarList()')
cmds.setParent('..')

cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
Multi_SnapB = cmds.button('MS_B', w=tmpRowWidth[0], l='Apply', c='Multi_Snap_Command()')


cmds.setParent('..')

cmds.setParent(MainRow)

Scd_Column = cmds.columnLayout(width=MainRL_Width[0])




Num_Label = cmds.frameLayout(label='Num_Count', w=MainRL_Width[0]-10)
Num_Check_Bttn_W = 50
Num_Check_Bttn = cmds.radioButtonGrp(select=1, labelArray3=['1','2','3'], numberOfRadioButtons=3, columnWidth3=[Num_Check_Bttn_W,Num_Check_Bttn_W,Num_Check_Bttn_W])

cmds.setParent('..')

Type_Label = cmds.frameLayout(label='Type', w=MainRL_Width[0]-10)
Type_Bttn_W = 100
Type_Bttn = cmds.radioButtonGrp(select=1, labelArray3=['Obj_Center','Pivot_Match','Pivot(Only)'], numberOfRadioButtons=3, columnWidth3=[Type_Bttn_W, Type_Bttn_W, Type_Bttn_W],
onCommand1='Off_Cmd()', onCommand2='On_Pivot_Match_Cmd()', onCommand3='Off_Cmd()', vertical=True)

cmds.setParent('..')

cmds.separator(h=10, style='none')



Pivot_Option = cmds.text(l='▷ Pivot_Match_Snap', enable=False)

Pos_check = cmds.checkBox(l='Position', value=1, enable=False)
Rot_check = cmds.checkBox(l='Rotate', value=1, enable=False)
Scl_check = cmds.checkBox(l='Scale', value=1, enable=False)


cmds.setParent(Main_Column)

cmds.separator(h=5, w=400)
cmds.text(l='Multi_Snap_ver.001 by HyunWoo', w=390, align='right')

cmds.showWindow(WinName)





def Off_Cmd():
    cmds.text(Pivot_Option, edit=True, enable=False)
    cmds.checkBox(Pos_check, edit=True, enable=False)
    cmds.checkBox(Rot_check, edit=True, enable=False)
    cmds.checkBox(Scl_check, edit=True, enable=False)

def On_Pivot_Match_Cmd():

    cmds.text(Pivot_Option, edit=True, enable=True)
    cmds.checkBox(Pos_check, edit=True, enable=True)
    cmds.checkBox(Rot_check, edit=True, enable=True)
    cmds.checkBox(Scl_check, edit=True, enable=True)


def updateSrcList():

    # Clear attribute list
    cmds.textScrollList('Src_List',e=True,ra=True)
     
    # Get current selection
    Src_Sel = cmds.ls(sl=True)
    if not Src_Sel: return
     
    # Update textScrollList
    for Sel in Src_Sel: cmds.textScrollList('Src_List', e=True, a=Sel)
     
    # Return result
    return Src_Sel

def updateTarList():

    # Clear attribute list
    cmds.textScrollList('Tar_List',e=True,ra=True)
     
    # Get current selection
    Tar_Sel = cmds.ls(sl=True)

    if not Tar_Sel: return
     
    # Update textScrollList
    for Sel in Tar_Sel:
        cmds.textScrollList('Tar_List',e=True,a=Sel)
     
    # Return result
    return Tar_Sel


def appendSrcList():

    Src_Sel = cmds.ls(sl=True)
    if not Src_Sel: return

    for Sel in Src_Sel:
        cmds.textScrollList('Src_List', e=True, a=Sel)

    return Src_Sel

def appendTarList():

    Tar_Sel = cmds.ls(sl=True)
    if not Tar_Sel: return

    for Sel in Tar_Sel:
        cmds.textScrollList('Tar_List', e=True, a=Sel)

    return Tar_Sel


def clearSrcList():

    cmds.textScrollList('Src_List',e=True,ra=True)

def clearTarList():

    cmds.textScrollList('Tar_List',e=True,ra=True)


def Multi_Snap_Command():

    Src_Snap_List = cmds.textScrollList('Src_List', q=True, ai=True)
    Tar_Snap_List = cmds.textScrollList('Tar_List', q=True, ai=True)

    Num_Count_Set1 = cmds.radioButtonGrp(Num_Check_Bttn, ed=True, q=True, select=1)
    Num_Count_Set2 = cmds.radioButtonGrp(Num_Check_Bttn, ed=True, q=True, select=2)
    Num_Count_Set3 = cmds.radioButtonGrp(Num_Check_Bttn, ed=True, q=True, select=3)

    Type_Set1 = cmds.radioButtonGrp(Type_Bttn, ed=True, q=True, select=1)
    Type_Set2 = cmds.radioButtonGrp(Type_Bttn, ed=True, q=True, select=2)
    Type_Set3 = cmds.radioButtonGrp(Type_Bttn, ed=True, q=True, select=3)

    Pos_Check_Set = cmds.checkBox(Pos_check, q=True, enable=True)
    Rot_Check_Set = cmds.checkBox(Rot_check, q=True, enable=True)
    Scl_Check_Set = cmds.checkBox(Scl_check, q=True, enable=True)


    for Src in Src_Snap_List:
        for Tar in Tar_Snap_List:

            Src_l = list(Src)
            Tar_l = list(Tar)

            if(Num_Count_Set1 == 1):

                if Src_l[-1] == Tar_l[-1]:

                    if Type_Set1 == 1:

                        cmds.select(Src, Tar)
                        cmds.align(alignToLead=True, x='mid', y='mid', z='mid')

                    elif Type_Set2 == 2:

                        if Pos_Check_Set == 1 and Rot_Check_Set == 0 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=True, rot=False, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 1 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=False, rot=True, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 0 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=False, rot=False, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 1 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=True, rot=True, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 1 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=False, rot=True, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 0 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=True, rot=False, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 1 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=True, rot=True, scl=True, piv=True)

                        else:
                            print('Pivot_Snap have to check at least one')

                    elif Type_Set3 == 3:

                        Src_Obj = cmds.ls(Src)
                        Tar_Obj = Tar

                        parentList = []

                        if cmds.listRelatives(Src_Obj, parent=True):
                            parentList.append(cmds.listRelatives(Src_Obj, parent=True)[0])

                        else:
                            parentList.append('')

                        pivotTranslate = cmds.xform(Tar_Obj, q=True, ws=True, rotatePivot=True)
                        cmds.parent(Src_Obj, Tar_Obj)
                        cmds.makeIdentity(Src_Obj, a=True, t=True, r=True, s=True)
                        cmds.xform(Src_Obj, ws=True, pivots=pivotTranslate)

                        if parentList[0] != '':
                            cmds.parent(Src_Obj[0], parentList[0])

                        else:
                            cmds.parent(Src_Obj[0], world=True)

                    else:

                        print('Error : Have to check Type')


            elif(Num_Count_Set2 == 2):

                if Src_l[-2] == Tar_l[-2] and Src_l[-1] == Tar_l[-1]:

                    if Type_Set1 == 1:

                        cmds.select(Src, Tar)
                        cmds.align(alignToLead=True, x='mid', y='mid', z='mid')

                    elif Type_Set2 == 2:

                        if Pos_Check_Set == 1 and Rot_Check_Set == 0 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=True, rot=False, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 1 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=False, rot=True, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 0 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=False, rot=False, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 1 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=True, rot=True, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 1 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=False, rot=True, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 0 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=True, rot=False, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 1 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=True, rot=True, scl=True, piv=True)

                        else:
                            print('Pivot_Snap have to check at least one')

                    elif Type_Set3 == 3:

                        Src_Obj = cmds.ls(Src)
                        Tar_Obj = Tar

                        parentList = []

                        if cmds.listRelatives(Src_Obj, parent=True):
                            parentList.append(cmds.listRelatives(Src_Obj, parent=True)[0])

                        else:
                            parentList.append('')

                        pivotTranslate = cmds.xform(Tar_Obj, q=True, ws=True, rotatePivot=True)
                        cmds.parent(Src_Obj, Tar_Obj)
                        cmds.makeIdentity(Src_Obj, a=True, t=True, r=True, s=True)
                        cmds.xform(Src_Obj, ws=True, pivots=pivotTranslate)

                        if parentList[0] != '':
                            cmds.parent(Src_Obj[0], parentList[0])

                        else:
                            cmds.parent(Src_Obj[0], world=True)

                    else:

                        print('Error : Have to check Type')


            elif(Num_Count_Set3 == 3):

                if Src_l[-3] == Tar_l[-3] and Src_l[-2] == Tar_l[-2] and Src_l[-1] == Tar_l[-1]:

                    if Type_Set1 == 1:

                        cmds.select(Src, Tar)
                        cmds.align(alignToLead=True, x='mid', y='mid', z='mid')

                    elif Type_Set2 == 2:

                        if Pos_Check_Set == 1 and Rot_Check_Set == 0 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=True, rot=False, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 1 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=False, rot=True, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 0 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=False, rot=False, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 1 and Scl_Check_Set == 0:
                            cmds.matchTransform(Src, Tar, pos=True, rot=True, scl=False, piv=True)

                        elif Pos_Check_Set == 0 and Rot_Check_Set == 1 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=False, rot=True, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 0 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=True, rot=False, scl=True, piv=True)

                        elif Pos_Check_Set == 1 and Rot_Check_Set == 1 and Scl_Check_Set == 1:
                            cmds.matchTransform(Src, Tar, pos=True, rot=True, scl=True, piv=True)

                        else:
                            print  ('Pivot_Snap have to check at least one')

                    elif Type_Set3 == 3:

                        Src_Obj = cmds.ls(Src)
                        Tar_Obj = Tar

                        parentList = []

                        if cmds.listRelatives(Src_Obj, parent=True):
                            parentList.append(cmds.listRelatives(Src_Obj, parent=True)[0])

                        else:
                            parentList.append('')

                        pivotTranslate = cmds.xform(Tar_Obj, q=True, ws=True, rotatePivot=True)
                        cmds.parent(Src_Obj, Tar_Obj)
                        cmds.makeIdentity(Src_Obj, a=True, t=True, r=True, s=True)
                        cmds.xform(Src_Obj, ws=True, pivots=pivotTranslate)

                        if parentList[0] != '':
                            cmds.parent(Src_Obj[0], parentList[0])

                        else:
                            cmds.parent(Src_Obj[0], world=True)

                    else:

                        print('Error : Have to check Type')