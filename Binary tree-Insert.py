class BinHeap:
    
    def __init__(self):
        
        self.heapList = [0]       # 初始BinHeap => 1st格是0
        
        self.currentSize = 0      # 一開始currentSize是0
         
    def percUp(self,i):
        
        while i // 2 > 0:                                 # i就是currentSize       //2是確認currentSize是不是大於1，currentSize == 1時，不用檢測heap property
            
            if self.heapList[i] < self.heapList[i // 2]:  #因為是binary tree，所以 位置//2，也就是sequence//2 就代表是上一level (parent node)
                                                          #此處是看parent node是不是 > child node (如果是，就要modify，因為是min-heap)
                tmp = self.heapList[i // 2]               #先記錄parent node的值
                
                self.heapList[i // 2] = self.heapList[i]  #把parent node的值換成child node的值
                
                self.heapList[i] = tmp                    #把child node的值換成原parent node的值
                
            i = i // 2                                    # i // 2 => 繼續再往上一level檢查heap property，因為我們剛剛有做一次swap，所以要確認再上一level是否符合heap property

    def insert(self,k):                           #用insert來增加binary tree的elements
        
        self.heapList.append(k)                   #用append來加入element => appending guarantees that we'll maintain the complete shape property
                                                  
        self.currentSize = self.currentSize + 1   # currentsize + 1
        
        self.percUp(self.currentSize)             #因為有加入element，apeending likely violate the heap property，所以要確認 heap property 
                                                  
     
r = BinHeap()

r.insert(5)
r.insert(9)
r.insert(11)
r.insert(14)
r.insert(7)

print (r)
