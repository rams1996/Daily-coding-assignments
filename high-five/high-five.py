class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        from collections import defaultdict
        items.sort(key=lambda x : x[1],reverse=True)
        
        hmap=defaultdict(list)
        
        for student,mark in items:
            hmap[student].append(mark)
        
        res=[]
        for val in hmap:
            count=0
            for i in range(5):
                count+=hmap[val][i]
                # print(count)
            res.append([val,count//5])
        return sorted(res)
                
        