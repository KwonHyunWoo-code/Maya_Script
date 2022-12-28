import maya.cmds as cmds

if cmds.window("Vray_Subdivs_Tool1", exists = True):
    cmds.deleteUI("Vray_Subdivs_Tool1")
    
mainwindow = cmds.window("Vray_Subdivs_Tool1", title = "VRay Subdivision Value Tool", w = 100, h = 150, rtf = 1, mxb = 0)

mainWidth = 500

mainform = cmds.formLayout(w = mainWidth, h = 480)
cmds.columnLayout( columnAttach=('both', 10), rowSpacing = 10, columnWidth = mainWidth)


Title = cmds.text(align = 'left', h = 20, label = "--- VRay Attributes Tool for Xerox Team by HJSon 2018---")
TopSep = cmds.separator(w = 450)


RowWidth1 = [mainWidth*0.3, mainWidth*0.2, mainWidth*0.2]


###=========================================== Subdivision Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (2, 'right', 30)])
Subdivision = cmds.text(label = 'Subdivision', align = 'left', w = RowWidth1[0])
SubdivisionBttn1 = cmds.button(w = RowWidth1[1], h = 25, al = 'center', label = 'On', command = 'vraySubdivOn()')
SubdivisionBttn2 = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Off', command = 'vraySubdivOff()')

cmds.setParent('..')

###=========================================== Subdivision Enable Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (3, 'left', 30)])
SubdivEnable = cmds.text(label = "Subdiv Enable", align = 'left', w = RowWidth1[0])
SubdivEnableBox = cmds.intField(w = 55, value = 0, min = 0, max = 100, step = 1)
SubdivEnableBttn = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Apply', command = 'vraysubdivisenable()')

cmds.setParent('..')

###=========================================== Subdivision Quality Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (2, 'right', 30)])
SubdivsQuality = cmds.text(label = 'SubdivsQuality', align = 'left', w = RowWidth1[0])

SubdivsQualityBttn1 = cmds.button(w = RowWidth1[1], h = 25, al = 'center', label = 'On', command = 'vraysubdivisqualityOn()')
SubdivsQualityBttn2 = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Off', command = 'vraysubdivisqualityOff()')

cmds.setParent('..')

###=========================================== Max Subdivs Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (3, 'left', 30)])
MaxSubdivs = cmds.text(label = "Max Subdivs", align = 'left', w = RowWidth1[0])
MaxSubdivsBox = cmds.intField(w = 55, value = 4, min = 1, max = 50, step = 1)
NaxSybduvsBttn = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Apply', command = 'maxsubdivs()')

cmds.setParent('..')


MidSep1 = cmds.separator(w = 450)

###=========================================== Displacement Control Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (2, 'right', 30)])
DispCtl = cmds.text(label = 'Displacement Control', align = 'left', w = RowWidth1[0])
DispCtlBttn1 = cmds.button(w = RowWidth1[1], h = 25, al = 'center', label = 'On', command = 'dispcontrolOn()')
DispCtlBttn2 = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Off', command = 'dispcontrolOff()')

cmds.setParent('..')

###=========================================== Displacement Amount Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (3, 'left', 30)])
DispAmount = cmds.text(label = 'Displacement Amount', align = 'left', w = RowWidth1[0])
DispAmountBox = cmds.floatField(w = 55, value = 1, min = -10, max = 10)
DispAmountBttn = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Apply', command = 'dispamount()')

cmds.setParent('..')

MidSep2 = cmds.separator(w = 450)

###=========================================== Object ID Section ===============================================###


cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (2, 'right', 30)])
ObjectID = cmds.text(label = 'Object ID', align = 'left', w = RowWidth1[0])
ObjectIDBttn1 = cmds.button(w = RowWidth1[1], h = 25, al = 'center', label = 'On', command = 'objIdOn()')
ObjectIDBttn2 = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Off', command = 'objIdOff()')

cmds.setParent('..')

###=========================================== Object ID Number Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7), (3, 'left', 30)])
ObjIDNo = cmds.text(label = 'Object ID Number', align = 'left', w = RowWidth1[0])
ObjectIDNumBox = cmds.intField(w = 55, value = 0, min = 0, max = 20)
ObjIDNoBttn = cmds.button(w = RowWidth1[2], h = 25, al = 'center', label = 'Apply', command = 'objectIdnumber()')

cmds.setParent('..')


MidSep3 = cmds.separator(w = 450)


###=========================================== Outliner Color Section ===============================================###

cmds.rowLayout(numberOfColumns=3, columnWidth3 = RowWidth1, columnAttach = [(1, 'left', 7)])
OutlinerCol = cmds.text(label = 'Outliner Color Maker', align = 'left', w = RowWidth1[0])
OLResetBttn = cmds.button(w = RowWidth1[1]*0.4, h = 25, al = 'center', label = 'Reset', command = 'outlinerReset()')
cmds.setParent('..')

RowWidth2 = [mainWidth*0.14, mainWidth*0.14, mainWidth*0.14, mainWidth*0.14, mainWidth*0.14, mainWidth*0.14]
cmds.rowLayout(numberOfColumns=6, columnWidth6 = RowWidth2, columnAttach = [(1, 'left', 7)])

OLColBttn1 = cmds.button(w = RowWidth2[0], h = 25, al = 'center', label = '', command = 'outlinerColor1()', bgc = [1, 0.224, 0.224])
OLColBttn2 = cmds.button(w = RowWidth2[1], h = 25, al = 'center', label = '', command = 'outlinerColor2()', bgc = [1, 0.399, 0.321])
OLColBttn3 = cmds.button(w = RowWidth2[2], h = 25, al = 'center', label = '', command = 'outlinerColor3()', bgc = [1, 1, 0.390])
OLColBttn4 = cmds.button(w = RowWidth2[3], h = 25, al = 'center', label = '', command = 'outlinerColor4()', bgc = [0.527, 1, 0.276])
OLColBttn5 = cmds.button(w = RowWidth2[4], h = 25, al = 'center', label = '', command = 'outlinerColor5()', bgc = [0.256, 0.628, 1])
OLColBttn6 = cmds.button(w = RowWidth2[5], h = 25, al = 'center', label = '', command = 'outlinerColor6()', bgc = [0.763, 0.332, 0.892])

cmds.setParent('..')



###=========================================== ETC ===============================================###


EndSep = cmds.separator(w = 450)
VerSion = cmds.text(h=20, align='right', label="Ver.1.04(Origin : HJSon / Python ver.HWKwon)")





cmds.showWindow("Vray_Subdivs_Tool1")


###---------------------------------------Command-----------------------------------------------###

### Vray Subdivs ###

def vraySubdivOn():
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_subdivision', 1)
            
def vraySubdivOff():
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_subdivision', 0)

### Vray Subdivs Quality ###

def vraysubdivisqualityOn():
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_subquality', 1)

def vraysubdivisqualityOff():
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_subquality', 0)

### Vray Displacement Control ###
        
def dispcontrolOn():    
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_displacement', 1)
        
def dispcontrolOff():    
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_displacement', 0)

### Object ID ###
        
def objIdOn():
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_objectID', 1)
        
def objIdOff():
    ListA = cmds.ls(sl = True, dag = True, leaf = True, shapes = True)
    for each in ListA:
        cmds.vray('addAttributesFromGroup', each, 'vray_objectID', 0)
        
        
### Outliner Color ###
 
def outlinerColor1():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        cmds.setAttr(each + '.useOutlinerColor', 1)
        cmds.setAttr(each + '.outlinerColor', 1, 0.224, 0.224)
    cmds.select(ListA, r=True)
        
def outlinerColor2():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        cmds.setAttr(each + '.useOutlinerColor', 1)
        cmds.setAttr(each + '.outlinerColor', 1, 0.399, 0.321)
    cmds.select(ListA, r=True)
        
def outlinerColor3():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        cmds.setAttr(each + '.useOutlinerColor', 1)
        cmds.setAttr(each + '.outlinerColor', 1, 1, 0.390)
    cmds.select(ListA, r=True)
        
def outlinerColor4():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        cmds.setAttr(each + '.useOutlinerColor', 1)
        cmds.setAttr(each + '.outlinerColor', 0.527, 1, 0.276)
    cmds.select(ListA, r=True)
        
def outlinerColor5():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        cmds.setAttr(each + '.useOutlinerColor', 1)
        cmds.setAttr(each + '.outlinerColor', 0.256, 0.628, 1)
    cmds.select(ListA, r=True)
        
def outlinerColor6():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        cmds.setAttr(each + '.useOutlinerColor', 1)
        cmds.setAttr(each + '.outlinerColor', 0.763, 0.332, 0.892)
    cmds.select(ListA, r=True)
            
def outlinerReset():
    ListA = cmds.ls(sl = True)
    for each in ListA:
        print(each)        
        cmds.setAttr(each + '.useOutlinerColor', 0)
    cmds.select(ListA, r=True)
    
### Vray Subdivs Enable ###

def vraysubdivisenable():
    ListA = cmds.ls(sl = True)
    SubdivEnableValue = cmds.intField(SubdivEnableBox, q=True, v=True)
     
    for each in ListA:
        
        cmds.setAttr(each + '.vraySubdivEnable', SubdivEnableValue)
        
def maxsubdivs():
    ListA = cmds.ls(sl = True)
    MaxSubdivsValue = cmds.intField(MaxSubdivsBox, q=True, v=True)
    for each in ListA:
        cmds.setAttr(each + '.vrayMaxSubdivs', MaxSubdivsValue)
        
def dispamount():
    ListA = cmds.ls(sl = True)
    DispAmountValue = cmds.floatField(DispAmountBox, q=True, v=True)
    for each in ListA:
        cmds.setAttr(each + '.vrayDisplacementAmount', DispAmountValue)
        
def objectIdnumber():
    ListA = cmds.ls(sl = True)
    ObjectIDNumValue = cmds.intField(ObjectIDNumBox, q=True, v=True)
    for each in ListA:
        cmds.setAttr(each + '.vrayObjectID', ObjectIDNumValue)
 