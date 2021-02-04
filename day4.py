from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1,5)
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x + 4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x - 4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z + 4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z = z - 4
        
        
        
        
        
        
        
        
        
myID = mc.getPlayerEntityId('Kai_Shing_Ciou')
mc.postToChat(myID, 'HELLO')
























list2d = [[1,0,1,1,1,1,1],
          [1,0,0,0,0,0,1],
          [1,0,1,1,1,0,1],
          [1,0,0,0,0,1,1],
          [1,0,1,1,0,0,1],
          [1,0,0,0,1,0,1],
          [1,1,1,1,1,0,1]]

x,y,z = mc.player.getTilePos()
startX = x
startZ = z

for i in range(4):
    for list1d in list2d:
        
        for i in list1d:
            mc.setBlock(x,y,z,i)
            x = x + 1
            
        x = startX
        z = z+1
        
    z = startZ
    y = y+1







































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        