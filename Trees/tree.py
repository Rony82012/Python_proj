mytree = ['a',['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]],[]]]

print(mytree)
print('Left subtree = ', mytree[1])
#print('Children of Left = ',mytree[1][1:])
print('Root = ', mytree[0])
print('Right subtree = ',mytree[2])
#print("Children of Right = ", mytree[2][1:])

def BinaryTree(r):
	return [r,[],[]] #extra empty sublist for children

def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t)>1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t)>1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

#testing
r = BinaryTree(1)
insertLeft(r,3)
insertLeft(r,5)
insertRight(r,4)
insertRight(r,6)
#insertRight(r,insertLeft(r,10))
L = getLeftChild(r)
print('L ', L)
R = getRightChild(r)
print('R ', R)

setRootVal(L,9)
print(r)
insertLeft(L,11)
print(r)

print(getRightChild(getRightChild(r)))



def buildTree():
	r = BinaryTree('a')
	insertLeft(r,'b')
	insertRight(getLeftChild(r),'d')
	insertRight(r,'c')
	insertLeft(getRightChild(r),'e')
	insertRight(getRightChild(r),'f')

	return r


print(buildTree())