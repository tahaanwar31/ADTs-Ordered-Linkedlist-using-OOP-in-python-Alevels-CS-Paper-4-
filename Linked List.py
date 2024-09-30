class node():
    #PUBLIC data:INTEGER
    #PUBLIC nextNode:INTEGER
    def __init__(self,dataP,nextNodeP):
        self.data=dataP
        self.nextNode=nextNodeP
#DECLARE linkedList:ARRAY[0:9] OF node
linkedList=[""]*10
linkedList[0]=node(1,1)
linkedList[1]=node(5,4)
linkedList[2]=node(6,7)
linkedList[3]=node(7,-1)
linkedList[4]=node(2,2)
linkedList[5]=node(0,6)
linkedList[6]=node(0,8)
linkedList[7]=node(56,3)
linkedList[8]=node(0,9)
linkedList[9]=node(0,-1)
startPointer=0
emptyList=5
def AddNode(currentPointer):
    global linkedList
    global emptyList
    DatatoAdd=int(input("Please input the data you want to add: "))
    if emptyList<0 or emptyList>9:
        print("No space")
    else:
        freeList=emptyList
        emptyList=linkedList[emptyList].nextNode
        newNode=node(DatatoAdd,-1)
        linkedList[freeList]=newNode
        previousPointer=currentPointer
        while currentPointer!=-1:
            previousPointer=currentPointer
            currentPointer=linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode=freeList
        print("Added")
def OrderedAddNode(currentPointer):
        global linkedList
        global emptyList
        global startPointer
        DatatoAdd = int(input("Please input the data you want to add: "))
        if emptyList < 0 or emptyList > 9:
            print("No space")
        else:
            freeList = emptyList
            emptyList = linkedList[emptyList].nextNode
            newNode = node(DatatoAdd, -1)
            linkedList[freeList] = newNode
            previousPointer = currentPointer
            while currentPointer != -1 and DatatoAdd<linkedList[currentPointer].data:
                previousPointer = currentPointer
                currentPointer = linkedList[currentPointer].nextNode
            if currentPointer==startPointer:
                linkedList[freeList].nextNode=startPointer
                startPointer=freeList
            else:
                linkedList[freeList].nextNode=linkedList[previousPointer].nextNode
                linkedList[previousPointer].nextNode=freeList

def deleteNode():
    global linkedList
    global startPointer
    global emptyList
    datatoremove=int(input("Please enter the data you want to remove: "))
    currentPointer=startPointer
    previousPointer=currentPointer
    while currentPointer!=-1 and linkedList[currentPointer].data!=datatoremove:
        previousPointer=currentPointer
        currentPointer=linkedList[currentPointer].nextNode
    if currentPointer==-1:
        print("No such value found")
    else:
        if currentPointer==startPointer:
            startPointer=linkedList[currentPointer].nextNode
        else:
            linkedList[previousPointer].nextNode=linkedList[currentPointer].nextNode
        linkedList[currentPointer].data=0
        linkedList[currentPointer].nextNode=emptyList
        emptyList=currentPointer
        print("Done")
def findItem(currentPointer,searchValue):
    while currentPointer!=-1:
        if linkedList[currentPointer].data==searchValue:
            return currentPointer
        else:
            currentPointer=linkedList[currentPointer].nextNode
    return currentPointer