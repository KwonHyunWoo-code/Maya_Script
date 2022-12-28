import maya.cmds as mc
mc.window(width=150) 
mc.columnLayout(adjustableColumn=True) 
mc.frameLayout(label="MultiUVSnapshot") 
mc.text(label="select_MultiUV") 
mc.radioButtonGrp("MultiUV",labelArray3=["UDIM","UVtile","singleUV"],numberOfRadioButtons=3) 
mc.button(label="SnapShot",command="MultiUVSnapshot('MultiUV')") 
mc.showWindow() 
 
 
def MultiUVSnapshot(a): 
    MultiUV = mc.radioButtonGrp("MultiUV",q=True,select=True) 
    fpth = mc.workspace(q=True,fn=True)
    rsl = 4096
    suv = mc.ls(sl=True,fl=True)
    for so in suv:
        uvt=[]
        mc.select(so,r=True)
        selShape = mc.listRelatives(so)
        uvCount = int(mc.polyEvaluate(selShape,uv=True))
        uvb = mc.polyEvaluate(so,b2=True)
        
        for i in range(0,uvCount,1):
            uvCrd = mc.polyEditUV(so + ".map[%d]" % i,q=True)
            uc = int(uvCrd[0]) + 1
            vc = int(uvCrd[1]) + 1
            if uvb[0][1]%1 == 0.0 and uvCrd[0] == uvb[0][1]: uc = uc -1
            if uvb[1][1]%1 == 0.0 and uvCrd[1] == uvb[1][1]: vc = vc -1
            if uvt.count([uc,vc]) == 0:uvt.append([uc,vc])
        for uvmx in uvt:
            if MultiUV == 1: 
                mc.uvSnapshot(aa=True,uMin=uvmx[0]-1,uMax=uvmx[0],vMin=uvmx[1]-1,vMax=uvmx[1],n=( fpth + "/sourceimages/" + so + "_" +str(1000 + ((uvmx[1] -1) * 10) + uvmx[0])+".png"),xr=rsl,yr=rsl,r=255,g=0,b=0,o=True,ff="png") 
            if MultiUV == 2: 
                mc.uvSnapshot(aa=True,uMin=uvmx[0]-1,uMax=uvmx[0],vMin=uvmx[1]-1,vMax=uvmx[1],n=( fpth + "/sourceimages/" + so + "_" +str('{0:03}'.format(uvmx[0]))+"_"+str('{0:03}'.format(uvmx[1]))+".png"),xr=rsl,yr=rsl,r=255,g=0,b=0,o=True,ff="png") 
        if MultiUV == 3: 
            mc.uvSnapshot(aa=True,uMin=0,uMax=1,vMin=0,vMax=1,n=( fpth + "/sourceimages/" + so + ".png"),xr=rsl,yr=rsl,r=255,g=0,b=0,o=True,ff="png") 
    print "Done" 
    
