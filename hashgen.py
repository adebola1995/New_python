import hashlib

path = r"C:\python\message.txt"

my_first_sha = "c16253d2753a9b222b5a78f6b08bc7b73b2d9feb6b74a2910593d5031a155fa5"
with open(path, 'rb') as opened_file:
   content = opened_file.read()
   sha256 = hashlib.sha256()
   
   sha256.update(content)
   
   my_sha = sha256.hexdigest()
print(my_sha)

if my_first_sha==my_sha:
   print("file is okay")
else:
   print("file tampered")