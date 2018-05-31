class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print('root ',r.getRootVal())
print('left ',r.getLeftChild())
r.insertLeft('b')
print('left ',r.getLeftChild())
print('left root ',r.getLeftChild().getRootVal())
r.insertRight('c')
print('right ',r.getRightChild())
print('right root ',r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print('updated right root ',r.getRightChild().getRootVal())


def buildTree(rootObj):
	r = BinaryTree(rootObj)
	r.insertLeft('b')
	r.insertRight('b').getRightChild('d')
	print(r.getRightChild().getRightChild().getRootVal())
	r.insertRight('c')

	return r

buildTree('a')

