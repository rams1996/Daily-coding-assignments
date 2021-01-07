    def addToFront(self,node):
        temp=self.head.nxt
        temp.prev=node
        self.head.nxt=node
        node.nxt=temp
        node.prev=self.head
​
    def get(self, key: int) -> int:
        if key in self.link:
            node=self.removeNode(self.link[key])
            self.addToFront(node)
            self.link[key]=node
            return node.val
        else:
            return -1
        
​
    def put(self, key: int, value: int) -> None:
        newNode=LList(key,value)
        if key in self.link:
            node=self.removeNode(self.link[key])
            self.addToFront(newNode)
            self.link[key]=newNode
        else:   
            if len(self.link)>=self.capacity:
                NodeToBeDeleted=self.tail.prev
                node=self.removeNode(NodeToBeDeleted)
                del self.link[node.key]
            self.addToFront(newNode)
            self.link[key]=newNode
            return None
            
        
​
​
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
