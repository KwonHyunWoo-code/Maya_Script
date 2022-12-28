import maya.cmds as cmds

### Render Layer Setting UI ###
  
winName = "RL_setting"   
winWidth = 400
titleName = "Render Layer Setting"

if cmds.window(winName, exists = True):
    cmds.deleteUI(winName)    
    
mainWindow = cmds.window(winName, title = titleName, w = winWidth, rtf = 1, mxb = 1, mnb = 1)
mainFL = cmds.formLayout(w = winWidth + 30)
mainCL = cmds.columnLayout(w = winWidth, rowSpacing = 5)

Title = cmds.text(label = titleName, width = winWidth, align = 'left', h = 20, font  = 'boldLabelFont')
cmds.separator(width = winWidth)

### Layout ###


## Total layout ##

MainRowWidth = [winWidth*0.25, winWidth*0.35, winWidth*0.35]
mainRL = cmds.rowLayout(w = winWidth, numberOfColumns=3, columnWidth3=MainRowWidth, columnAttach = [(1, 'left', 15), (3, 'right', 10)])


## First Column - Name_Tag ##

cmds.columnLayout(w=MainRowWidth[0])

tmpRowWidth1 = [MainRowWidth[0]]
cmds.rowLayout(numberOfColumns=1)
cmds.text(label='¢¹ Name_Tag ¢·', align='center', h=30, width = tmpRowWidth1[0])
cmds.setParent('..')

tmpRowWidth1 = [MainRowWidth[0]*0.2, MainRowWidth[0]*0.55]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth1, columnAttach = [(1, 'left', 10), (2, 'right', 5)])
MarkCheckBox = cmds.checkBox(align = 'center', w = tmpRowWidth1[0], h = 30)
MarkTxtField = cmds.textField(w = tmpRowWidth1[1], h = 30)
cmds.setParent('..')

## First Column - Custom_Lyr ##

tmpRowWidth1 = [MainRowWidth[0]]
cmds.rowLayout(numberOfColumns=1)
cmds.text(label='Custom', align='center', h=30, width = tmpRowWidth1[0])
cmds.setParent('..')

tmpRowWidth1 = [MainRowWidth[0]]
cmds.rowLayout(numberOfColumns=1, columnAttach = (1,'left',15))
CustomTxt = cmds.textField(w = tmpRowWidth1[0]*0.7, h = 30)
cmds.setParent('..')

tmpRowWidth1 = [MainRowWidth[0]]
cmds.rowLayout(numberOfColumns=1, columnAttach = (1,'left',15))
CustomBttn = cmds.button(label='Apply', align='center', h=25, w=tmpRowWidth1[0]*0.7, c='Custom_Ly_Create()')
cmds.setParent('..')

### ¡é¡é¡é  Blank ¡é¡é¡é  ###

#cmds.setParent('..')
#cmds.text(label=' ')
cmds.text(label=' ')

### ¡è¡è¡è  Blank ¡è¡è¡è  ###



cmds.setParent(mainRL)



## Second Column - Layer 01 ##

cmds.columnLayout(w=MainRowWidth[1])

tmpRowWidth2 = [MainRowWidth[1]*0.4, MainRowWidth[1]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth2)
ColLyTxt = cmds.text(label='Col', align='center', h=30, width = tmpRowWidth2[0])    
ColLyBttn = cmds.button(label='Apply', h=25, width = tmpRowWidth2[1], c='Col_Ly_Create()')
cmds.setParent('..')
tmpRowWidth2 = [MainRowWidth[1]*0.4, MainRowWidth[1]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth2)
RefLTxt = cmds.text(label='RefL', align='center', h=30, width=tmpRowWidth2[0])    
RefLBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth2[1], c='REFL_Ly_Create()')
cmds.setParent('..')
tmpRowWidth2 = [MainRowWidth[1]*0.4, MainRowWidth[1]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth2)
SPECTxt = cmds.text(label='SPEC', align='center', h=30, width=tmpRowWidth2[0])    
SPECBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth2[1], c='SPEC_Ly_Create()')
cmds.setParent('..')
tmpRowWidth2 = [MainRowWidth[1]*0.4, MainRowWidth[1]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth2)
RefRTxt = cmds.text(label='RefR', align='center', h=30, width=tmpRowWidth2[0])    
RefRBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth2[1], c='REFR_Ly_Create()')
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth2)
DspTxt = cmds.text(label='Disp.', align='center', h=30, width=tmpRowWidth2[0])    
DspBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth2[1], c='Disp_Ly_Create()')

#cmds.button(label='Apply', h=25, width=tmpRowWidth2[1], c='Custom_Ly_Create()')
cmds.setParent(mainRL)


## Third Column - Layer 02 ##

cmds.columnLayout(w=MainRowWidth[2])
tmpRowWidth3 = [MainRowWidth[2]*0.4, MainRowWidth[2]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth3)
NorTxt = cmds.text(label='Nor', align='center', h=30, width=tmpRowWidth3[0])    
NorBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth3[1], c='Nor_Ly_Create()')
cmds.setParent('..')
tmpRowWidth3 = [MainRowWidth[2]*0.4, MainRowWidth[2]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth3)
IDTxt = cmds.text(label='ID', align='center', h=30, width=tmpRowWidth3[0])    
IDBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth3[1], c='ID_Ly_Create()')
cmds.setParent('..')
tmpRowWidth3 = [MainRowWidth[2]*0.4, MainRowWidth[2]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth3)
AOTxt = cmds.text(label='AO', align='center', h=30, width=tmpRowWidth3[0])
AOBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth3[1], c='AO_Ly_Create()')
cmds.setParent('..')
tmpRowWidth3 = [MainRowWidth[2]*0.4, MainRowWidth[2]*0.4]
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth3)
ETCTxt = cmds.text(label='ETC', align='center', h=30, width=tmpRowWidth3[0])
ETCBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth3[1], c='ETC_Ly_Create()')
tmpRowWidth3 = [MainRowWidth[2]*0.4, MainRowWidth[2]*0.4]
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth3)
PrevTxt = cmds.text(label='Prev', align='center', h=30, width=tmpRowWidth3[0])
PrevBttn = cmds.button(label='Apply', h=25, width=tmpRowWidth3[1], c='Prev_Ly_Create()')
cmds.setParent(mainCL)






cmds.separator(width = winWidth)

cmds.formLayout(mainFL, edit = True, attachForm = [(mainCL, 'left', 15), (mainCL, 'right', 15)])

cmds.showWindow(mainWindow)



### Render Layer Create ###

def Col_Ly_Create():

    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
    
    if MarkChk == 0:
        Crl_col = cmds.createRenderLayer( n = 'Col#', nr = True )
    else:
        Crl_col = cmds.createRenderLayer( n = MarkTxt + '_Col#', nr = True )
    return

def Nor_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
    
    if MarkChk == 0:
        Crl_nor = cmds.createRenderLayer( n = 'Nor#', nr = True )
    else:
        Crl_nor = cmds.createRenderLayer( n = MarkTxt + '_Nor#', nr = True )
    return
    
def SPEC_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)   
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
    
    if MarkChk == 0:
        Crl_spec = cmds.createRenderLayer( n = 'SPEC#', nr = True )
    else:
        Crl_spec = cmds.createRenderLayer( n = MarkTxt + '_SPEC#', nr = True )
    return
    
def REFL_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1) 
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_refl = cmds.createRenderLayer( n = 'RefL#', nr = True )
    else:
        Crl_refl = cmds.createRenderLayer( n = MarkTxt + '_RefL#', nr = True )
    return
            
def REFR_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_refr = cmds.createRenderLayer( n = 'RefR#', nr = True )
    else:
        Crl_refr = cmds.createRenderLayer( n = MarkTxt + '_RefR#', nr = True )
    return
    
def ID_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_id = cmds.createRenderLayer( n = 'ID#', nr = True )
    else:
        Crl_id = cmds.createRenderLayer( n = MarkTxt + '_ID#', nr = True )
    return
    
def AO_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_ao = cmds.createRenderLayer( n = 'AO#', nr = True )
    else:
        Crl_ao = cmds.createRenderLayer( n = MarkTxt + '_AO#', nr = True )
    return
    
def ETC_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_etc = cmds.createRenderLayer( n = 'ETC#', nr = True )
    else:
        Crl_etc = cmds.createRenderLayer( n = MarkTxt + '_ETC#', nr = True )
    return
    
def Prev_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_prev = cmds.createRenderLayer( n = 'Prev', nr = True )
    else:
        Crl_prev = cmds.createRenderLayer( n = MarkTxt + '_Prev', nr = True )
    return

def Disp_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
       
    if MarkChk == 0:
        Crl_disp = cmds.createRenderLayer( n = 'Disp#', nr = True )
    else:
        Crl_disp = cmds.createRenderLayer( n = MarkTxt + '_Disp#', nr = True )
    return

def Custom_Ly_Create():
    
    MarkChk = cmds.checkBox(MarkCheckBox, q=1, value=1)
    MarkTxt = cmds.textField(MarkTxtField, q=1, text=1)
    CtmTxt = cmds.textField(CustomTxt, q=1, text=1)
       
    if MarkChk == 0:
        Crl_custom = cmds.createRenderLayer( n = CtmTxt, nr = True )
    else:
        Crl_custom = cmds.createRenderLayer( n = MarkTxt + '_' + CtmTxt, nr = True )
    return
    
    
###-------------------------------------------------------------###

###-------------------Random Object ID Create-------------------###

#ListA = cmds.ls(sl=1)

