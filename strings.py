#implementmethods of dictionary
#capitalize()
place = 'mysore'
x = place.capitalize()
print(x)
#casefold()
y = place.casefold()
print(y)
#center()
a = place.center(10)
print(a)
#count()
text = "sleep is neccessary,good sleep is even more necessary"
s = text.count("sleep")
print(s)
#encode()
quote = "Work is worship"
q = quote.encode()
print(q)
#endswith()
sentence = "Sun rises in the east."
r = sentence.endswith(".")
print(r)
#expandtabs()
word = "e\ta\ts\tt"
w = word.expandtabs(8)
print(w)
#find()
f = text.find("sleep")
print(f)
#formats()
vote = "eligible only for those with {age:.2f} years"
print(vote.format(age = 18))
#index()
sentence1 = "there is abig crocodile in the lake"
i = sentence1.index("in")
print(i)
#isalnum()
item = "maggie4444"
t = item.isalnum()
print(t)
#isalpha()
company = "nike"
a = company.isalpha()
print(a)
#isdecimal()
unicode ="\u0033"
u = unicode.isdecimal()
print(u)
#isdigit()
number = "4442356"
n = number.isdigit()
print(n)
#islower()
txt = "world is large"
w = txt.islower()
print(w)
#isnumeric()
m = number.isnumeric()
print(m)
#isprintable()
txt1 = "hi\how are you #3"
h = txt1.isprintable()
print(h)
#isspace()
space = "   "
b = space.isspace()
print(b)
#istitle()
truth = "Sun Sets In The West"
t = truth.istitle()
print(t)
#isupper()
txt2 = "NOW THE TIME STARTS"
n = txt2.isupper()
print(n)
#join()
myTuple = ("Vivek","Vinay","Vijay")
p = "#".join(myTuple)
print(p)
#1just()
city = "NewDelhi"
d = city.ljust(10)
print(d, "is the capital of india")
#lower()
city1 = "HYDERABAD"
u = city1.lower()
print(u)
#lstrip()
corona = "     omnicorn     "
c2 = corona.lstrip()
print("of all virsuses",c2, "is variant of concern")
#maketrans()
txt3 = "A Man!"
mytable = txt3.maketrans("M", "V")
print(txt3.translate(mytable))
#partition()
words = "I wish to sleep all day"
w = words.partition("sleep")
print(w)
#replace()
thing = "I like mountains"
h = thing.replace("mountains", "beaches")
print(h)
#rfind()
sentence5 = "they are working in NCDS"
d = sentence5.rfind("are")
print(d)
#rindex()
e = sentence5.rindex("in")
print(e)
#rjust()
places = "gandhinagar"
g = places.rjust(20)
print(g, "is a city in gujarat.")
#rpartition()
mountain = "Mt.Everest is in himalayas, himalayas are located in north India"
u = mountain.rpartition("himalayas")
print(u)
#rsplit()
places = "mumbai,delhi, kolkata"
l = places.rsplit(", ")
print(l)
#rstrip()
corona = "     omnicorn     "
c2 = corona.rstrip()
print("of all virsuses",c2, "is variant of concern")
#split()
world = "welcome to my world"
w = world.split()
print(w)
#splitness()
year = "good bye 2021 \nWelcome to 2022"
r = year.splitlines()
print(r)
#startswith()
o = year.startswith("good")
print(o)
#strip()
corona = "     omnicorn     "
c2 = corona.strip()
print("of all virsuses",c2, "is variant of concern")
#swapcase()
sentence4 = "THE himalyas, the YAMUNA,The nilagirls are LOCATED in india"
s5 = sentence4.swapcase()
print(s5)
#title()
year = "good bye 2021 \nWelcome to 2022"
r1 = year.title()
print(r1)
















 













