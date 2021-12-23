import re

'''
# \n \t \" \' \. - \ is called as escape operator
# Sample 1
print("\"Monisha\"")
print(re.escape('www.python.org'))
print(re.escape('This is sample Text'))
'''
'''
# Sample 2
#pa='[a-zA-Z]+'
#pa='[a-z]+'
#pa='[a-s]+'
#pa='[a-s]'
pa='[.?\-",*]+'
text ='I am supraja form chennai? Kolathur -99 ,Tamilnadu.'
print(re.findall(pa,text))
'''
'''
# Sample 3
s=input("Enter a search text : ")
text= input("Enter a Text : ")
print(re.findall(s,text))
'''
''' 
#Sample 4
#\w - matches any alphanumeric
text= input("Enter a Text : ")
#pa=re.match('(\w\w\w)-(\d\d\d)',text)
#pa=re.match('\w\w\w',text)
pa=re.match('(\w\w\w(\d\d\d))',text) # Nee123 
print(pa.group()) # Entire match
print(pa.group(1)) # subgroup -1
print(pa.group(2)) # subgroup -2
print(pa.groups()) # All subgroups
'''
'''
#Sample 5
s=input("Enter a search text : ")
text= input("Enter a Text : ")
res=re.match(s,text)

print(res)
if res is not None:
    print("It is Matching")
else:
    print("It is not Matching")
'''
'''
# Sample 6 - website Email Address
text= input("Enter a Email : ")
pa='\w+@(\w+\.)?\w+\.com'
print(re.match(pa,text).group())
'''
'''
#%d %s %ld %f - Format specificator - in C lang
txt=input("Enter a text :")
s=input("Enter search text :")
fstr= "%-20s: %s" # user defined format
c=re.compile(txt)
print(fstr%("Original Text", txt))
print(fstr%("Compiled Text", c))

print(fstr%("Search Text", re.search(s,txt)))
print(fstr%("Compiled Search Text", c.search(txt)))
'''
'''
# diff between search and match
1. both are function
2. both can return first string
3. But match will start to find from the begining only
4. But search can take the text from middle also.
'''
'''
#Sample 7
Li=[]
ex=[]

for i in range(5):
    Li.append(input("Enter Text " + str(i+1)  +":" ))

for i in range(3):
    ex.append(input("Enter Pattern " + str(i+1)  +":" ))
print(Li)
print(ex)

for e in ex:
    for s in Li:
        if re.match(e,s):
            print(e," matches ",s)
        else:
            print(e," not matches ",s)
            
'''
#Sample 8
#print(re.match(input("Enter search text : "),input("Enter Text : ")).group())

'''
#Sample 9
# Split
text=input("Enter text : ")
print(re.split('[, ]+',text))
print(re.split('[, ]+',text,maxsplit=2))
print(re.split('[, ]+',text,maxsplit=1))
print(re.split('[, ]+',text,maxsplit=0)) # default
'''
'''
#Sample 10
text=input("Enter text : ")
fro=input("Enter from text : ")
to=input("Enter to text : ")
print(text.replace(fro,to))
'''
'''
#Sample 11
s=input("Enter starting character : ") + '.*?' + input("Enter ending character : ")
+ '$'
if re.search(s, input("Enter text : ")):
    print('Found a match')
else:
    print('Not matched')
'''
'''
#Sample 12
text= re.compile("^96")
if text.match(input("Enter Mobile No : ")):
    print("Valid Mobile No")
else:
    print("Invalid Mobile No")
'''
'''
#Sample 13
pa=re.finditer("([0-9]{1,3})",input("Enter Number : ")) # iter = Iteration
for n in pa:
    print(n.group(0))
'''
 
#Sample 14
text='''
Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.
'''
#print(re.findall(r"\b\w{3,4}\b",text))
#print(re.findall(r"\b\w{6,}\b",text))


#sample 15
text='''
Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.
'''
print(re.sub("[ ,.]",":",text))













