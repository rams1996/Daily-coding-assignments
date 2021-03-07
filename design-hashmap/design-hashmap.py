class LinkedList:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        
class MyHashMap:

    def __init__(self):
        self.hashTable=[LinkedList(None,None) for i in range(10001)]
    def findHashValue(self,key):
        return key%100
    def findPreviousNode(self,key): 
        hashValue=self.findHashValue(key)
        node=self.hashTable[hashValue]
        while node.next:
            if node.next.key==key:
                return node
            node=node.next
        # print(node.value,node.next)
        return node
        
    def put(self, key: int, value: int) -> None:
        
        node=self.findPreviousNode(key)
        if node.next==None:
            node.next=LinkedList(key,value)
        else:
            node.next.value=value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        node=self.findPreviousNode(key)
        if node.next==None:
            return -1
        return node.next.value
        

    def remove(self, key: int) -> None:
        
        node=self.findPreviousNode(key)
        if node.next==None:
            return
        node=self.findPreviousNode(key)
        node.next=node.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)