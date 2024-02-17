# generates regex for numbers (ge / le / in range) 

## Tested against Windows / Python 3.11 / Anaconda

## pip install regex4numbers

```python
from regex4numbers import number_between, number_ge, number_le
import re
import random

for _ in range(5):
    start = random.randint(-1000, 1000)
    end = random.randint(1002, 2000)
    regex = number_between(start=start, end=end, fullnumberreplacement="\\d")
    print(f"{regex=}\n")
    regexcompiled = re.compile(regex)
    for x in range(5):
        randomint = random.randint(-(start * 2), end * 2)
        regexresults = regexcompiled.findall(str(randomint))
        print(f"""start: {start} end: {end} number:{randomint} / {regexresults=}""")
        isbetween = randomint >= start and randomint < end
        anyfound = any(regexresults)
        assert isbetween == anyfound

for _ in range(5):
    n = random.randint(-1000, 1000)
    ge_regex = number_ge(n=n, fullnumberreplacement="\\d")
    le_regex = number_le(n=n, fullnumberreplacement="\\d")
    print(f"{ge_regex=}\n")
    print(f"{le_regex=}\n")

    biggerthan = re.compile(ge_regex)
    lessthen = re.compile(le_regex)
    start = random.randint(-1000, 1000)
    end = random.randint(1002, 2000)
    for x in range(5):
        randomint = random.randint(-(start * 2), end * 2)
        regexresultsbigger_or_equal = biggerthan.findall(str(randomint))
        regexresultslessthan_or_equal = lessthen.findall(str(randomint))
        print(
            f"""n:{n} test:{randomint} bigger or equal: {regexresultsbigger_or_equal} less or equal: {regexresultslessthan_or_equal}"""
        )
        isbigger = randomint >= n
        islessthan = randomint <= n
        anyfoundbigger = any(regexresultsbigger_or_equal)
        anyfoundlessthan = any(regexresultslessthan_or_equal)
        assert isbigger == anyfoundbigger
        assert islessthan == anyfoundlessthan
    print(f"""start: {start} end: {end} number:{randomint} / {regexresults=}""")




# regex='(?:-(?:\\b(?:1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3[01]?|[456789]))?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))\\b)|(?:(?<!-)\\b(?:(?:1(?:(?:0(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|3(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|4(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|5(?:(?:0\\d?|1\\d?|2\\d?|3[01]?|[456789]))?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|3(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|4(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|5(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|6(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|7(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|8(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|9(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|0))\\b)'

# start: -231 end: 1532 number:617 / regexresults=['617']
# start: -231 end: 1532 number:592 / regexresults=['592']
# start: -231 end: 1532 number:793 / regexresults=['793']
# start: -231 end: 1532 number:1662 / regexresults=[]
# start: -231 end: 1532 number:1605 / regexresults=[]
# regex='(?:(?<!-)\\b(?:(?:1(?:0(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|1(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|2(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|3(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|4(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|5(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|6(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|7(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|70?|[89])|8\\d|9\\d)|2(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|3(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|4(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|5(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|6(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|7(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|8(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)|9(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)))\\b)'

# start: 30 end: 1771 number:3226 / regexresults=[]
# start: 30 end: 1771 number:183 / regexresults=['183']
# start: 30 end: 1771 number:1369 / regexresults=['1369']
# start: 30 end: 1771 number:3425 / regexresults=[]
# start: 30 end: 1771 number:1280 / regexresults=['1280']
# regex='(?:(?<!-)\\b(?:(?:10(?:0\\d|1\\d)|3(?:3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|4(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|5(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|6(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|7(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|8(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|9(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)))\\b)'

# start: 330 end: 1020 number:771 / regexresults=['771']
# start: 330 end: 1020 number:1825 / regexresults=[]
# start: 330 end: 1020 number:313 / regexresults=[]
# start: 330 end: 1020 number:825 / regexresults=['825']
# start: 330 end: 1020 number:823 / regexresults=['823']
# regex='(?:-(?:\\b(?:1\\d?|2\\d?|3\\d?|4[0123456]?|[56789]))\\b)|(?:(?<!-)\\b(?:(?:1(?:(?:0(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|3(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|4(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|5(?:(?:0\\d?|1[012345]?|[23456789]))?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|3(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|4(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|5(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|6(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|7(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|8(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|9(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|0))\\b)'

# start: -46 end: 1516 number:967 / regexresults=['967']
# start: -46 end: 1516 number:128 / regexresults=['128']
# start: -46 end: 1516 number:1633 / regexresults=[]
# start: -46 end: 1516 number:2720 / regexresults=[]
# start: -46 end: 1516 number:466 / regexresults=['466']
# regex='(?:(?<!-)\\b(?:(?:1(?:0(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|1(?:0\\d|1[0123]))|7(?:1[56789]|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|8(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|9(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)))\\b)'

# start: 715 end: 1114 number:1520 / regexresults=[]
# start: 715 end: 1114 number:238 / regexresults=[]
# start: 715 end: 1114 number:1446 / regexresults=[]
# start: 715 end: 1114 number:731 / regexresults=['731']
# start: 715 end: 1114 number:-3 / regexresults=[]
# ge_regex='(?:-(?:\\b(?:1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1[0123456]?|[23456789]))?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)\\b))|(?:\\b0\\b)|(?:(?<!-)(?:\\b[1-9]\\d{0,}\\b))'

# le_regex='(?:-(?:\\b(?:1000|2(?:1[6789]|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|3(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|4(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|5(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|6(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|7(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|8(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|9(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d))\\b))|(?:-\\b[1-9]\\d{3,}\\b)'

# n:-216 test:278 bigger or equal: ['278'] less or equal: []
# n:-216 test:838 bigger or equal: ['838'] less or equal: []
# n:-216 test:411 bigger or equal: ['411'] less or equal: []
# n:-216 test:1178 bigger or equal: ['1178'] less or equal: []
# n:-216 test:2238 bigger or equal: ['2238'] less or equal: []
# start: 175 end: 1264 number:2238 / regexresults=[]
# ge_regex='(?:(?<!-)(?:\\b(?:5(?:8[3456789]|9\\d)|6(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|7(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|8(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|9(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d))\\b))|(?:(?<!-)(?:\\b[1-9]\\d{3,}\\b))'

# le_regex='(?:(?:\\b(?:1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|3(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|4(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|5(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8[0123]?|9))?|6\\d?|7\\d?|8\\d?|9\\d?)\\b))|(?:\\b0\\b)|(?:-\\b[1-9]\\d{0,}\\b)'

# n:583 test:623 bigger or equal: ['623'] less or equal: []
# n:583 test:1594 bigger or equal: ['1594'] less or equal: []
# n:583 test:779 bigger or equal: ['779'] less or equal: []
# n:583 test:-141 bigger or equal: [] less or equal: ['-141']
# n:583 test:836 bigger or equal: ['836'] less or equal: []
# start: 105 end: 1284 number:836 / regexresults=[]
# ge_regex='(?:(?<!-)(?:\\b(?:599|6(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|7(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|8(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|9(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d))\\b))|(?:(?<!-)(?:\\b[1-9]\\d{3,}\\b))'

# le_regex='(?:(?:\\b(?:1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|2(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|3(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|4(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|5(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?))?|6\\d?|7\\d?|8\\d?|9\\d?)\\b))|(?:\\b0\\b)|(?:-\\b[1-9]\\d{0,}\\b)'

# n:599 test:2300 bigger or equal: ['2300'] less or equal: []
# n:599 test:1054 bigger or equal: ['1054'] less or equal: []
# n:599 test:2563 bigger or equal: ['2563'] less or equal: []
# n:599 test:951 bigger or equal: ['951'] less or equal: []
# n:599 test:509 bigger or equal: [] less or equal: ['509']
# start: -241 end: 1532 number:509 / regexresults=[]
# ge_regex='(?:(?<!-)(?:\\b(?:1(?:4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|2(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|3(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|4(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|5(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|6(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|7(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|8(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d)|9(?:0\\d|1\\d|2\\d|3\\d|4\\d|5\\d|6\\d|7\\d|8\\d|9\\d))\\b))|(?:(?<!-)(?:\\b[1-9]\\d{3,}\\b))'

# le_regex='(?:(?:\\b(?:1(?:(?:0\\d?|1\\d?|2\\d?|3\\d?|40?|[56789]))?|2\\d?|3\\d?|4\\d?|5\\d?|6\\d?|7\\d?|8\\d?|9\\d?)\\b))|(?:\\b0\\b)|(?:-\\b[1-9]\\d{0,}\\b)'

# n:140 test:2003 bigger or equal: ['2003'] less or equal: []
# n:140 test:-141 bigger or equal: [] less or equal: ['-141']
# n:140 test:-1048 bigger or equal: [] less or equal: ['-1048']
# n:140 test:3098 bigger or equal: ['3098'] less or equal: []
# n:140 test:2382 bigger or equal: ['2382'] less or equal: []
# start: 914 end: 1579 number:2382 / regexresults=[]
# ge_regex='(?:-(?:\\b(?:1\\d?|2\\d?|3\\d?|4\\d?|5[01234567]?|[6789])\\b))|(?:\\b0\\b)|(?:(?<!-)(?:\\b[1-9]\\d{0,}\\b))'

# le_regex='(?:-(?:\\b(?:100|5[789]|6\\d|7\\d|8\\d|9\\d)\\b))|(?:-\\b[1-9]\\d{2,}\\b)'

# n:-57 test:2559 bigger or equal: ['2559'] less or equal: []
# n:-57 test:1798 bigger or equal: ['1798'] less or equal: []
# n:-57 test:1983 bigger or equal: ['1983'] less or equal: []
# n:-57 test:1738 bigger or equal: ['1738'] less or equal: []
# n:-57 test:2001 bigger or equal: ['2001'] less or equal: []
# start: -795 end: 1484 number:2001 / regexresults=[]

```