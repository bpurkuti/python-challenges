import unittest
# write a function that convernts a word into different casings
# assume no spacing
# snake_case example fire_truck OR Fire_Truck  (capitalization does not matter)
# camelCase example fireTruck
# PascalCase example FireTruck
# kebab-case example fire-truck

# casing('registeredUser','camelCase','kebab-case') -> registered-user


# Splitting words into 2 different word based on ['capital letter after first letter', '-', and  '_']
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

# Remove '-' or '_' from the beginning of word if needed
def purify(word):
    if word[0]=='_' or word[0]=='-':
        word = word[1:]
    return word
# word_word --> don't change or care about capitalization of word
def snakeCase(word):
    w1 = word[0]
    w2 = purify(word[1])
    return (w1, f'_{w2}')

# wordWord
def camelCase(word):
    w1 = word[0]
    w2 = purify(word[1])
    w2 = w2.capitalize()
    
    if(w1[0].isupper()):
        w1 = w1[0].lower() + w1[1:]
    return (w1, w2)

#WordWord
def pascalCase(word):
    w1 = word[0].capitalize()
    w2 = purify(word[1])
    w2 = w2.capitalize()
    return (w1, w2)

#word-word
def kebabCase(word):
    w1 = word[0]
    w2 = word[1]
    w2 = purify(w2)
    
    w1 = w1.lower()
    w2 = w2.lower()
    return (w1, f'-{w2}')

#We split the word first the put word through different casings and return the output
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
        
    
    



########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_camel_to_Pascal(self):
        result = casing(word='redSphere',initial='camelCase',target='PascalCase')
        self.assertEquals(result,'RedSphere')

    def test_camel_to_kebab(self):
        result = casing('redSphere','camelCase','kebab-case')
        self.assertEquals(result,'red-sphere')

    def test_camel_to_snake(self):
        result = casing('redSphere','camelCase','snake_case')
        self.assertEquals(result,'red_Sphere')


    def test_Pascal_to_snake(self):
        result = casing('GreenApple','PascalCase','snake_case')
        self.assertEquals(result,'Green_Apple')

    def test_Pascal_to_kebab(self):
        result = casing('GreenApple','PascalCase','kebab-case')
        self.assertEquals(result,'green-apple')

    def test_Pascal_to_camel(self):
        result = casing('GreenApple','PascalCase','camelCase')
        self.assertEquals(result,'greenApple')
    

    def test_kebab_to_camel(self):
        result = casing('green-apple','kebab-case','camelCase')
        self.assertEquals(result,'greenApple')

    def test_kebab_to_Pascal(self):
        result = casing('green-apple','kebab-case','PascalCase')
        self.assertEquals(result,'GreenApple')   

    def test_kebab_to_snake(self):
        result = casing('green-apple','kebab-case','snake_case')
        self.assertEquals(result,'green_apple') 
    

    def test_snake_to_camel(self):
        result = casing('green_apple','snake_case','camelCase')
        self.assertEquals(result,'greenApple') 
    
    def test_snake_to_Pascal(self):
        result = casing('green_apple','snake_case','PascalCase')
        self.assertEquals(result,'GreenApple') 
    
    def test_snake_to_kebab(self):
        result = casing('green_apple','snake_case','kebab-case')
        self.assertEquals(result,'green-apple') 

if __name__ == '__main__':
    unittest.main()