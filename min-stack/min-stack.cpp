class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s1;
    stack<int> s2;
    MinStack() {
        s2.push(INT_MAX);
    }
    
    void push(int val) {
        int lowest=s2.top();
        if(val<lowest){
            s2.push(val);
        }
        else{
            s2.push(lowest);
        }
        s1.push(val);
        
    }
    
    void pop() {
        if(!s1.empty()){
            s1.pop();
            s2.pop();
        }
        
    }
    
    int top() {
        if(s1.size()>0){
            return s1.top();
        }
        return -1;
    }
    
    int getMin() {
        return s2.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */