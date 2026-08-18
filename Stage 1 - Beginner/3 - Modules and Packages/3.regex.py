import re

text = "404 not found "
match = re.search("\d+",text)
if match:
    print(match.group())
    
text = "Error 404 found"
print(re.match(r"\d+", text)) # Output: None (because it starts with letters)

text2 = "404 Error found"
print(re.match(r"\d+", text2).group()) # Output: "404"


text4 = "222-333 and 555-444 is mobile number"
print(re.findall(r"(\d{3})-(\d{3})",text4))
print(re.sub(r"(\d{3})-(\d{3})","XXX-XXX",text4))
match = re.search(r"(\d{3})-(\d{3})",text4)
if match:
    print(match.group(1))
    print(match.group(2))
    

