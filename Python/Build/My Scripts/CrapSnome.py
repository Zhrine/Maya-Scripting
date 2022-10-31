import maya.cmds as cmds

snoSize = [3, 2, 1.40]
snoSpace = [0, 3, 2]
snoBe1 = cmds.polySphere( sx=15, sy=15, r=snoSize[0])
cmds.xform(snoBe1, r=True, os=True, t =(0,(snoSize[0]+snoSpace[0]),0))

snoBe1 = cmds.polySphere( sx=15, sy=15, r=snoSize[1])
cmds.xform(snoBe1, r=True, os=True, t =(0,(snoSize[0]+snoSpace[1]) ,0))

snoBe1 = cmds.polySphere( sx=15, sy=15, r=snoSize[2])
cmds.xform(snoBe1, r=True, os=True, t =(0,(snoSize[0]+snoSize[1]+snoSpace[2] +1) ,0))
#hi