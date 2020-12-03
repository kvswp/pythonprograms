s = "My name is Kota Venkat Swaroop, I did M.Tech from SRM University. qt framework , jenkins server"
#s = "The quick brown fox jumps over the lazy dog"
#up = 0
#low = 0
d = {'upper':0,'lower':0}

for char in s:
 if char.isupper():
#  up = up + 1
   d['upper'] += 1
 elif char.islower():
#  low += 1
   d['lower'] += 1
 else:
  pass

print("uppercase letters = {} and lower case letters = {}".format(d['upper'],d['lower'])) 

print(s)
repchars = [',','.',' ']
for i in repchars:
 s = s.replace(i, '')
print(s)
s = s.lower()
s1 = list(set(s))
s1 = sorted(s1)
print(s1)

#test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
#print(test_list)

#test_list = []
#alpha = 'a'
#for i in range(0, 26): 
#    test_list.append(alpha) 
#    alpha = chr(ord(alpha) + 1)
#print(test_list)

test_list = []
test_list = list(map(chr, range(97, 123)))
print(test_list) 

#import string
#alphabet_string = string.ascii_lowercase
#alst = list(alphabet_string)
#print(alst)

if test_list == s1:
 print("pangram sentence")
else:
 print("all alphabets not present in sentence")
