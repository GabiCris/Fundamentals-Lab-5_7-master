
import unittest
from iterStruct.StructureLab9 import iterStruct

class Test(unittest.TestCase):
 
    def setUp(self):
        self._iterTest = iterStruct()
      
    def testSort(self):
        
        for i in range(34,145):
            self._iterTest.append(i%24)
            
        self._iterTest.sortIter()
        self.assertEqual(self._iterTest,sorted(self._iterTest))
        
        def sortFunct(a,b):
            if a > b:
                return False
            return True
        
        self.assertRaises(TypeError, self._iterTest.sortIter, 45)
        
    def testFilter(self):
        for i in range(34,145):
            self._iterTest.append(i%24)
            
        self._iterTest.filterIter(lambda a: a%10%2==0)
        self.assertEqual(self._iterTest[0], 10)
        self.assertEqual(self._iterTest[1], 12)
        self.assertEqual(self._iterTest[-2], 22)
        
        self._iterTest.filterIter(lambda a: a%10 == 0)
        self.assertEqual(self._iterTest[0], 10)
        self.assertEqual(self._iterTest[1], 20)
        
        self.assertRaises(TypeError, self._iterTest.filterIter)
        self.assertRaises(TypeError, self._iterTest.filterIter, 345)
        