import maya.cmds as cmds

list = ["Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt","Leg_##_Jnt"]
zeros = 0
argu_num = 1
hashtag = "#"

for argument in list:
   for hashtag in argument:
      zeros += 1
   new_argu = argument.replace("#", "0", zeros)
   new_argu = new_argu.replace("0","", len(str(argu_num)))
   new_under = new_argu.find("_", new_argu.find("_")+1)
   print(new_argu[:new_under]+ str(argu_num) +new_argu[new_under:])
   argu_num += 1