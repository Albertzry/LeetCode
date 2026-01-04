int prime[]={2, 3, 5, 7, 11, 13, 17, 17, 19, 23, 29, 31, 37, 41, 43,
 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
  127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 
  193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 
  269, 271, 277, 281, 283, 293, 307, 311, 313 };
int Div4[100001];

class Solution {
public:
    static int sum4Div(int x){
        if (Div4[x]!=-1) return Div4[x];
        int y=x, sum=1+x, cntPF=0, xsqrt=sqrt(x);
        for(int p: prime){
            if (p>xsqrt) break;
            if (y%p) continue;
            int e=0;
            while(y%p==0){
                y/=p;
                e++;
            }
            cntPF++;
            if (y==1 && cntPF==1){
                if (e==1)  return 0;
                if (e==3)  return Div4[x]=1+p+p*p+p*p*p;
            }
            if (e>1) return Div4[x]=0;
            sum+=p;
        }
        if (y>1){
            cntPF++;
            sum+=y;
        }
        return Div4[x]=(cntPF==2)?sum:0;
    }

    static int sumFourDivisors(vector<int>& nums) {
        if (Div4[0]==0) memset(Div4, -1, sizeof(Div4));
        int ans=0;
        for(int x: nums)
            ans+=sum4Div(x);
        return ans;
    }
};