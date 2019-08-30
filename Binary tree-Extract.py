class BinHeap:
    
    def __init__(self):
        
        self.heapList = [0]           
        self.currentSize = 0
        
    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:             #�Ĥ@run ��i == 1     i * 2 == 2 => �]���p�GcurrentSize == 1�ɡA�����˴�heap property
            
            mc = self.minChild(i)                      #��i == 1��original�̤pchild node
            
            if self.heapList[i] > self.heapList[mc]:   #��i == 1��original�̤pchild node��A�p�G���snode 1 > i == 1��original�̤pchild node => �nmodify (�]���Omin-heap)
                
                tmp = self.heapList[i]                 #���O��node 1����
                
                self.heapList[i] = self.heapList[mc]   #��node 1���ȴ���i == 1��original�̤pchild node����
                
                self.heapList[mc] = tmp                #��i == 1��original�̤pchild node���ȴ����snode 1����
                
            i = mc                                     # i == mc => �~��A���U�@level�ˬdheap property�A�]���ڭ̭�観���@��swap�A�ҥH�n�T�{�A�U�@level�O�_�ŦXheap property                        

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:                    #�Ĥ@run ��i == 1    i * 2 + 1 == 3 => �]���p�GcurrentSize == 2�ɡAi == 1��original�̤pchild node�N�Onode 2 

            return i * 2        

        else:            

            if self.heapList[i*2] < self.heapList[i*2+1]:   #�Ĥ@run ��i == 1    i * 2 + 1 == 3 => �]���p�GcurrentSize > 2�ɡAi == 1��original�̤pchild node�N�n�Τ��   
                                                            # ��� node 2    &    node 3 ���@�Ӥ���p
                return i * 2            

            else:               

                return i * 2 + 1

    def delMin(self):
        
        retval = self.heapList[1]                            #����list[1]���ȡA�]��binary tree��extraction�O�qlist[1]�}�l�R
        
        self.heapList[1] = self.heapList[self.currentSize]   #��list[1]���ȴ����̫�@��element����
        
        self.currentSize = self.currentSize - 1              # currentsize - 1
        
        self.heapList.pop()                                  # pop���̫�@��element�A�]���W�zsteps�w�g��list[1]���ȴ����̫�@��element����
        
        self.percDown(1)                                     #�]����list[1]���ȴ����̫�@��element���ȡA�ҥH�n�T�{ heap property     
                                                             # i == 1   => �q1�}�l�ˬd
        return retval
