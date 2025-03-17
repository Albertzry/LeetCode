class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('||s[i]=='['||s[i]=='{'){
                stack.push_back(s[i]);
                continue;
            }
            if(s[i]==')'){
                if(!stack.empty()&&stack.back()=='('){
                    stack.pop_back();
                    continue;
                }
                else{
                    return false;
                }
            }
            if(s[i]==']'){
                if(!stack.empty()&&stack.back()=='['){
                    stack.pop_back();
                    continue;
                }
                else{
                    return false;
                }
            }
            if(s[i]=='}'){
                if(!stack.empty()&&stack.back()=='{'){
                    stack.pop_back();
                    continue;
                }
                else{
                    return false;
                }
            }
        }
        if(stack.size()!=0){
            return false;
        }
        return true;
    }
};