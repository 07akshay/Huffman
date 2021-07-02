import heapq
from heapq import heapify
from heapq import heappush
from heapq import heappop

class Node:
    def __init__(self, val, freq: int):
        self.val = val
        self.left = None
        self.right = None
        self.freq = freq
        
    def __lt__(self, other):
        return (self.freq < other.freq)

def doc():
	print("This is a very simple library which can be used for text compression. \nYou need to give a text input in the expand() function and recieve the dictionary, compressed text and root object as the output.\n\nThen to get the original text back you only need to pass these 3 things as the input to the expand() function.\nThe output recieved would be the original text")	

def recur(codes, root : Node, a):
    if root.left:
        recur(codes, root.left, a+'0')
    if root.right:
        recur(codes, root.right, a+'1')
    if root.left==None and root.right==None:
        codes[root.val] = a

def compress(text):
	"""
	This function takes the text input - which can contain 
	any ascii character.

	It returns 3 things:
		1. A dictionary of unique characters which contains
		   thier corresponding codes.
		2. The compressed message
		3. The final object list, which contains the root
			node object 

	"""
	try:
	    d = dict.fromkeys(text,0)
	    for i in text:
	        d[i] +=1
	    final_list =[]
	    for i in d:
	        obj = Node(i, d[i])
	        final_list.append(obj)

	    heapify(final_list)
	    while len(final_list)>1:
	        obj1 = heappop(final_list)
	        obj2 = heappop(final_list)
	        obj = Node(None, obj1.freq+obj2.freq)
	        obj.left = obj1
	        obj.right = obj2
	        heappush(final_list, obj)
	        
	    codes = dict.fromkeys(text,'')
	    recur(codes, final_list[0].left, '0')
	    recur(codes, final_list[0].right, '1')
	    encryption = ''
	    for j in text:
	        encryption += codes[j]
	    encryption
	    
	    return codes, encryption, final_list

	except:
		print("Invalid Input!")

def expand(codes, encryption, start):
	"""
	It takes the dictionary, compressed message and root
	object as the input.

	Returns the original text.

	"""
	try:
	    root = start
	    decryption = ""
	    for code in encryption:
	        if code == '0':
	            obj = root.left
	            root = obj
	        elif code == '1':
	            obj = root.right
	            root = obj
	        if obj.val:
	            decryption += obj.val
	            root = start
	    return decryption

	except:
		print("Can't expand using invalid dictionary or compressed message")