import pymel.core as pm
def getCurves(tstep, deg=3):
    """Generate cv curves from particle paths. 
    Sample the path every tstep in the current time range and generate curve with degree deg.
    Before executing, select particle in object mode (i.e. curves from all points) or component mode (i.e. curves from selected points)."""

    global curvesData #FIX! I hate this global variable... find other way to collect data
    curvesData = {}
    tmin = int(pm.playbackOptions(q=1, min=1))
    tmax = int(pm.playbackOptions(q=1, max=1))
    makeCurves(tmin, tmax, tstep, deg)
    
def makeCurves(tmin, tmax, tstep, deg):
    if not pm.filterExpand(selectionMask = 47): # Boolean switches
        component = False
        prt = pm.ls(selection=1)[0] # Instantiate selected particle transform
        print('\n// In object mode')
    else:
        component = True
        prt = pm.ls(hilite=1)[0] # Instantiate selected particle transform
        print('\n// In component mode')    
    for t in range(tmax):
        pm.currentTime(t)
        if not prt.pointCount(): # Pass if there are no existing particles points 
            pass
        else:
            if t in range(tmin, tmax, tstep): # Fetch position data only if current time coincides step
                #print('// partPath:    At time {0}'.format(t))
                selectedParticles(prt, component)
        
    grp = pm.group(em=1, n='particlePaths1') # Create new group
    # Create curves from particle data:
    for curv in curvesData.keys():
        #print('// partPath:    Making curve{0}'.format(curv))
        pm.curve(n=curv, p=curvesData[curv], d=deg)
        pm.parent(curv, grp) # Parent to group grp

                
def selectedParticles(particle, mode):
    if mode: # If in component mode
        slPrt = pm.filterExpand(selectionMask = 47) # Make string array (i.e. list) of selected particle components
        prtIds = [int(p.split('.')[1].strip('pt[]')) for p in slPrt] # Parse id values from string array slPrt
        for id in prtIds:
            if id in range(particle.pointCount()):
                if 'curve{0}'.format(id) in curvesData:
                    #print('// selectedParticles:    Processing id {0}...'.format(id))
                    curvesData['curve{0}'.format(id)] += [particle.pt[id].position]
                else:
                    #print('// selectedParticles:    Processing id {0}...'.format(id))
                    curvesData['curve{0}'.format(id)] = [particle.pt[id].position]
                    #print('// selectedParticles:    curve{0} generated'.format(id))
            else:
                print('// particle {0} doesn\'t exist yet'.format(id))
    else: # If in object mode
        particle = pm.ls(sl=1)[0] # Instantiate selected particle
        for id in range(particle.pointCount()):
            if 'curve{0}'.format(id) in curvesData:
                #print('// selectedParticles:    Processing id {0}...'.format(id))
                curvesData['curve{0}'.format(id)] += [particle.pt[id].position]
            else:
                #print('// selectedParticles:    Processing id {0}...'.format(id))
                curvesData['curve{0}'.format(id)] = [particle.pt[id].position]
                #print('// selectedParticles:    curve{0} generated'.format(id))