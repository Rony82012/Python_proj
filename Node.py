'''The basic building block for the linked list implementation 
is the node. Each node object must hold at least two pieces of 
information. First, the node must contain the list item itself.
We will call this the data field of the node. In addition,
each node must hold a reference to the next node.
the program shows the Python implementation. To construct a node,
you need to supply the initial data value for the node. 
Evaluating the assignment statement below will yield a node 
object containing the value 93 (see Figure 3). You should note 
that we will typically represent a node object. 
the Node class also includes the usual methods to access and modify 
the data and the next reference.
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
'''

class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

'''
temp = Node(147)
temp.setData(369)
temp.setNext(124)
temp.setNext(234)
temp.setNext(456)
print(temp.getData())
print(temp.getNext())'''