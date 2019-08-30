class BinHeap:
    
    def __init__(self):
        
        self.heapList = [0]
        self.currentSize = 0

    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:             #材run i == 计材levelparent node => 矪耞Α﹚穦Θミセ琌ノlen(alist) // 2眔i
            
            mc = self.minChild(i)                      #тi == 计材levelparent node程child node
            
            if self.heapList[i] > self.heapList[mc]:   #Τi == 计材levelparent node程child node狦parent node > 程child node => 璶modify (琌min-heap)
                
                tmp = self.heapList[i]                 #癘魁original parent node
                
                self.heapList[i] = self.heapList[mc]   #рoriginal parent node传Θ程child node
                
                self.heapList[mc] = tmp                #р程child node传Θoriginal parent node
                
            i = mc                                     # i == mc => 膥尿┕level浪琩heap propertyиΤ暗Ωswap┮璶絋粄level琌才heap property                        

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:                    #材run i == 计材levelparent node => 狦currentSize == i * 2程child node碞琌node (i * 2)            

            return i * 2        

        else:            

            if self.heapList[i*2] < self.heapList[i*2+1]:   #材run i == 计材levelparent node => 狦currentSize > i * 2 程child node碞璶ノゑ耕                                                               # ゑ耕 node (i * 2)   &    node (i * 2 + 1) ゑ耕

                return i * 2             

            else:               

                return i * 2 + 1

    def buildHeap(self,alist):
        
        i = len(alist) // 2                 #矪len(alist) // 2種琌眖计材levelnode (parent node)秨﹍浪琩 (//2 & binary闽玒┮穦т计材level)
                                            #程level碞琌leaf nodes                                    
        self.currentSize = len(alist)       #魁currentSize
        
        self.heapList = [0] + alist[:]      #0┮Τbinary treelist常穦眖0秨﹍
        
        while (i > 0):                      #眖计材level秨﹍浪琩root                
            
            self.percDown(i)                #ノpercDown() =>  眖计材level程level                   
            i = i - 1                       # i = i-1 => 眖计材level计材levelㄌ┕root
                                            # (τ计材level计材levelΤswap┮临璶眖计材level程level => 碞琌i == mcêline)
r = BinHeap()

r.buildHeap([9, 6, 5, 2, 3])
