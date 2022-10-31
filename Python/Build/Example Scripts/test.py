# always ALWAYS add this
import maya.cmds as cmds
# lets us use maya commands in python

# python variables are Mutable and able to change on the fly
# sels = 3.4 automatically turns my variable into a float value
sels = cmds.ls(selection=True)
# I can now use commands like ls in python bc of maya.cmds import
sel = sels[0]

# in python always specify object first
pos = cmds.xform(sel, q=True, ws=True, rotatePivot=True)

loc = cmds.spaceLocator( p=(0,0,0) )[0]

# loc = locs [0] we can really just add the array straight onto the variable above
# locs = ["locator1"] same as this command so you can really just shorten it

cmds.xform(loc, ws=True, translation=pos )