class BinHeap:
    
    def __init__(self):
        
        self.heapList = [0]
        self.currentSize = 0

    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:             #�Ĥ@run ��i == �˼ƲĤGlevel��parent node => ���B���P�_���@�w�|���ߡA�]���쥻�O��len(alist) // 2�o��i
            
            mc = self.minChild(i)                      #��i == �˼ƲĤGlevel��parent node���̤pchild node
            
            if self.heapList[i] > self.heapList[mc]:   #��i == �˼ƲĤGlevel��parent node���̤pchild node��A�p�G��parent node > �̤pchild node => �nmodify (�]���Omin-heap)
                
                tmp = self.heapList[i]                 #���O��original parent node����
                
                self.heapList[i] = self.heapList[mc]   #��original parent node���ȴ����̤pchild node����
                
                self.heapList[mc] = tmp                #��̤pchild node���ȴ�����original parent node����
                
            i = mc                                     # i == mc => �~��A���U�@level�ˬdheap property�A�]���ڭ̭�観���@��swap�A�ҥH�n�T�{�A�U�@level�O�_�ŦXheap property                        

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:                    #�Ĥ@run ��i == �˼ƲĤGlevel��parent node => �]���p�GcurrentSize == i * 2�ɡA�̤pchild node�N�Onode (i * 2)            

            return i * 2        

        else:            

            if self.heapList[i*2] < self.heapList[i*2+1]:   #�Ĥ@run ��i == �˼ƲĤGlevel��parent node => �]���p�GcurrentSize > i * 2 �ɡA�̤pchild node�N�n�Τ��                                                               # ��� node (i * 2)   &    node (i * 2 + 1) ���@�Ӥ���p

                return i * 2             

            else:               

                return i * 2 + 1

    def buildHeap(self,alist):
        
        i = len(alist) // 2                 #���B��len(alist) // 2���N��O�q�˼ƲĤGlevel��node (parent node)�}�l�ˬd (�]��//2 & binary�����Y�A�ҥH�|���˼ƲĤGlevel)
                                            #�]���̫�@level�N�Oleaf nodes                                    
        self.currentSize = len(alist)       #����currentSize
        
        self.heapList = [0] + alist[:]      #�[0�A�]���Ҧ���binary tree��list���|�q0�}�l
        
        while (i > 0):                      #�q�˼ƲĤGlevel�}�l�ˬd����root                
            
            self.percDown(i)                #��percDown() =>  �q�˼ƲĤGlevel�ݳ̫�@level                   
            i = i - 1                       # i = i-1 => �q�˼ƲĤTlevel�ݭ˼ƲĤGlevel�A�̧ǩ��W��root
                                            # (�Ӧb�˼ƲĤTlevel�ݭ˼ƲĤGlevel�ɡA�i�঳swap�A�ҥH�٭n�A�q�˼ƲĤGlevel�ݳ̫�@level => �N�Oi == mc��line)
r = BinHeap()

r.buildHeap([9, 6, 5, 2, 3])
