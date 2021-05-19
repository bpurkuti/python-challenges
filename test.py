from collections import Counter
import math
#### Analysis.py

# def analyze(*nums):
    

#     total = 0
#     largest= nums[0]
#     smallest= nums[0]
#     size = len(nums)
    
#     for i  in sorted(nums):
#         if(i>largest):
#             largest = i
        
#         if(i<smallest):
#             smallest = i
#         # for mean
#         total+= i
#         #for median
        
#     #mean
#     mean = total/size
    
#     #median
#     nums = sorted(nums)
#     if(len(nums)%2 !=0):
#         median = nums[int((size-1)/2)+1]
#     else:
#         median = (nums[int(size/2)] + nums[int((size/2)+1)])/2
        
#     #mode
#     #using counter from collections and using its highest val
#     #Counter potrays elements as {key: value}
#     #Here, we are getting key with the highest value
#     c = Counter(nums)
#     mode = max(c, key=c.get)

#     print(mean, median, mode, largest, smallest)
    
    
# print(analyze(1,2,2,2,3))
# print(analyze(10,5,10,200,-65))

#### baseball.py
# def inning_to_outs(innings):
#     if innings == int(innings):
#         return innings*3
#     else:
#         deci = float(innings%1)
#         notDeci = innings//1
        
#         print(deci, notDeci)
#         return (notDeci *3 + deci*10)//1
    
    
# print(inning_to_outs(3))
# print(inning_to_outs(2.2))

#### casing.py
def split(word):
    first =""
    last = ""
    #split the word
    for i in word:
        if word.index(i)!= 0:
            if i.isupper():
                first = word[0:word.index(i)]
                last = word[word.index(i):]
                return (first, last)
            elif i == '-' or i== '_':
                first = word[0:word.index(i)]
                last = word[word.index(i)+1:]
                print(first, last)
                return (first, last)

def pascalHelper(word):
    if(word[0].islower()):
        word= word[0].upper() + word[1:]
    return word


def snakeCase(word):
    return (word[0], f'_{word[1]}')
        
def camelCase(word):
    w1 = word[0]
    w2 = pascalHelper(word[1])
    
    if(w1[0].isupper()):
        w1 = w1[0].lower() + w1[1:]
    return (w1, w2)

def pascalCase(word):
    w1 = pascalHelper(word[0])
    w2 = pascalHelper(word[1])
    return (w1, w2)
    
def kebabCase(word):
    w1 = word[0]
    w2 = word[1]

    w1 = w1.lower()
    w2 = w2.lower()
    return (w1, f'-{w2}')

def casing(word, initial, target):
    str = split(word)
    
    if initial == "snake_case":
        str = snakeCase(str)
    elif initial == "camelCase":
        str = camelCase(str)
    elif initial == "PascalCase":
        str = pascalCase(str)
    elif initial == "kebab-case":
        str = kebabCase(str)
        
    if target == "snake_case":
        str = snakeCase(str)
    elif target == "camelCase":
        str = camelCase(str)
    elif target == "PascalCase":
        str = pascalCase(str)
    elif target == "kebab-case":
        str = kebabCase(str)
        
    return (f'{str[0]}{str[1]}')
    

# result = casing('GreenApple','PascalCase','kebab-case')
result = kebabCase(('GreenApple','PascalCase'))

print(result, len(result))















###Currency
# def currency(value):
#     deci, notDeci = math.modf(value)
#     notDeci = int(notDeci)
#     deci = int(round(deci, 2)*100)
#     return(f'${notDeci}.{deci}')

# print(currency(100.238123123), currency(5.2))