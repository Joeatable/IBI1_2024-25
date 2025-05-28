import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("/Users/joey/Desktop/IBI1_2024-25/Practical 14/movies.xml")
collection = DOMTree.documentElement
movies = collection.getElementsByTagName('Movie')

for movie in movies:
	print('------Movie------')
	print('Title: ', movie.getElementsByTagName('Title')[0].firstChild.nodeValue)
	print('Year: ', movie.getElementsByTagName('Year')[0].firstChild.nodeValue)
	if movie.hasAttribute('rating'):
		print('Rating: ',movie.getAttribute('rating'))

