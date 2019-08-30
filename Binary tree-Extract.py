class BinHeap:
    
    def __init__(self):
        
        self.heapList = [0]           
        self.currentSize = 0
        
    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:             #材run i == 1     i * 2 == 2 => 狦currentSize == 1ぃノ浪代heap property
            
            mc = self.minChild(i)                      #тi == 1original程child node
            
            if self.heapList[i] > self.heapList[mc]:   #Τi == 1original程child node狦穝node 1 > i == 1original程child node => 璶modify (琌min-heap)
                
                tmp = self.heapList[i]                 #癘魁node 1
                
                self.heapList[i] = self.heapList[mc]   #рnode 1传Θi == 1original程child node
                
                self.heapList[mc] = tmp                #рi == 1original程child node传Θ穝node 1
                
            i = mc                                     # i == mc => 膥尿┕level浪琩heap propertyиΤ暗Ωswap┮璶絋粄level琌才heap property                        

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:                    #材run i == 1    i * 2 + 1 == 3 => 狦currentSize == 2i == 1original程child node碞琌node 2 

            return i * 2        

        else:            

            if self.heapList[i*2] < self.heapList[i*2+1]:   #材run i == 1    i * 2 + 1 == 3 => 狦currentSize > 2i == 1original程child node碞璶ノゑ耕   
                                                            # ゑ耕 node 2    &    node 3 ゑ耕
                return i * 2            

            else:               

                return i * 2 + 1

    def delMin(self):
        
        retval = self.heapList[1]                            #魁list[1]binary treeextraction琌眖list[1]秨﹍
        
        self.heapList[1] = self.heapList[self.currentSize]   #рlist[1]传Θ程element
        
        self.currentSize = self.currentSize - 1              # currentsize - 1
        
        self.heapList.pop()                                  # pop奔程element瓃steps竒рlist[1]传Θ程element
        
        self.percDown(1)                                     #рlist[1]传Θ程element┮璶絋粄 heap property     
                                                             # i == 1   => 眖1秨﹍浪琩
        return retval
