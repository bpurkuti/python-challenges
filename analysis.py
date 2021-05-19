import unittest
from collections import Counter

# the analyze function takes in an var arguent of numbers
# it should return a dicitonary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def analyze(*nums):
    
    total = 0
    largest= nums[0]
    smallest= nums[0]
    size = len(nums)
    
    for i  in sorted(nums):
        if(i>largest):
            largest = i
        
        if(i<smallest):
            smallest = i
        # for mean
        total+= i
        #for median
        
    #mean
    mean = total/size
    
    #median
    nums = sorted(nums)
    if(len(nums)%2 !=0):
        median = nums[int((size-1)/2)+1]
    else:
        median = (nums[int(size/2)] + nums[int((size/2)+1)])/2
        
    #mode
    #using counter from collections and using its highest val
    #Counter potrays elements as {key: value}
    #Here, we are getting key with the highest value
    c = Counter(nums)
    mode = max(c, key=c.get)
    
    return {'mean':mean,'median':median,'mode':mode, 'largest':largest,'smallest':smallest}
        

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1,2,2,2,3)
        self.assertDictEqual(data, {'mean':2,'median':2,'mode':2, 'largest':3,'smallest':1})
        

    def test_analyze_2(self):
        data = analyze(10,5,10,200,-65)
        self.assertDictEqual(data, {'mean':32,'median':10,'mode':10, 'largest':200,'smallest':-65})
        


if __name__ == '__main__':
    unittest.main()
