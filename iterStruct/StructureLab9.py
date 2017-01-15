
class iterStruct(list):
    def __init__(self):
        list.__init__(self)
    
    #COMBSORT
    def sortIter(self, comparisonFunct = None):
        gap = len(self)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))  # minimum gap is 1
            swaps = False
            for i in range(len(self) - gap):
                j = i+gap
                if comparisonFunct == None:
                    if self[i] > self[j]:
                        self[i], self[j] = self[j], self[i]
                        swaps = True
                else:
                    if comparisonFunct(self[i], self[j]):
                        self[i], self[j] = self[j], self[i]
                        swaps = True
                        
    def filterIter(self, filterFunct):
        self[:] = [elem for elem in self if filterFunct(elem) == True]
        

#===============================================================================
#  
# st = iterStruct()
# st.append(123)
# st.append(6432)
# st.append(1213)
# print(st)
# def funct(a,b):
#     if a>b:
#         return True
#     return False
# def funct1(a,b):
#     if a<b:
#         return True
#     return False
# st.sortIter(funct)
# print(st)
# st.sortIter(funct1)
# print(st)
#===============================================================================