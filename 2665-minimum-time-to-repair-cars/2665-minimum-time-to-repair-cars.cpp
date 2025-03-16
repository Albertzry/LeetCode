class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long maxr=*max_element(ranks.begin(),ranks.end());
        long long upper=maxr*cars*cars;
        long long lower=0;
        while (lower<=upper){
            long long middle=(upper+lower)/2;
            long long cnt=0;
            for (int r:ranks){
                cnt+=pow(middle/r,0.5);
            }
            if (cnt>=cars){
                upper=middle-1;
            }else{
                lower=middle+1;
            }
        }
        return lower;
    }
};