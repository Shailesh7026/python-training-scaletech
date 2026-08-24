from collections import Counter,OrderedDict,defaultdict,ChainMap,namedtuple

# Counter
print(Counter(['B','B','A']))
print(Counter({'B': 2, 'A': 1}))
print(Counter(B=2,A=1))

# OrderedDict
od = OrderedDict()
od['a'] = 1;
od['b'] = 2;

print(od)

del od['a'] # or do -> od.pop('a')
od['a'] = 1;

print(od)

# DefaultDic
dd = defaultdict(lambda: "Not Found")
# dd = defaultdict(int)

print(dd['a'])

# ChainMap
print(ChainMap(od,dd))

# NamedTuple

Student = namedtuple('Student',['name','age'])

s1 = Student("Shailesh",21)
s2 = Student("RR",21)

print(Student)
print(s1[1])
print(s2.name)