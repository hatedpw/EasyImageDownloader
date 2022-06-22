import requests

urls = []
with open("urls.txt") as f:
	urls = [i.strip('\n') for i in f.readlines()]
a = 0
for each in urls:
	# download image from url
	response = requests.get(each)
	a+=1
	file = open(f"{a}.png", "w+b")
	file.write(response.content)
	print(a)

