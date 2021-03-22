class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegrees(numCourses,0);
        unordered_map<int,vector<int>> courses;
        queue<int> q;
        
        for(auto course : prerequisites){
            cout<<course[0]<<course[1];
            indegrees[course[0]]++;
            if(courses.find(course[1])==courses.end()){
                courses[course[1]]={};
            }
            courses[course[1]].push_back(course[0]);
        }
        for(int i=0;i<indegrees.size();i++){
            if (indegrees[i]==0){
                q.push(i);
            }
        }
        while(!q.empty()){
            for(int i=0;i<q.size();i++){
                auto currNode=q.front();
                q.pop();
                vector<int> temp = courses[currNode];
                for (auto values:temp){
                    if(--indegrees[values]==0){
                        q.push(values);
                    }
                    
                }
            }
        }
        for(int i=0;i<indegrees.size();i++){
            if (indegrees[i]>0){
                return false;
            }
        }
      return true  ;
    }
};