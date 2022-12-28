import maya.cmds as cmds
import pymel.core as pm

if cmds.window("Shader_HW", exists = True):
    cmds.deleteUI("Shader_HW")

mainwindow = cmds.window("Shader_HW", title = "Shader_Library", w = 100, h = 150, rtf = 1, mxb = 0)