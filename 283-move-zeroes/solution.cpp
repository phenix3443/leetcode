#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroStart = 0;
        for (int i=0; i < nums.size(); ++i) {
            if (nums[i]!=0){
                if(i!=zeroStart) {
                    iter_swap(nums.begin()+i,nums.begin()+zeroStart);
                }

                zeroStart++;
            }
        }
    }
};
