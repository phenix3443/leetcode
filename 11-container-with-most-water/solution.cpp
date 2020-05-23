 // -*- coding:utf-8; -*-

#include <vector>

using namespace std;

class Solution {
public:
  int maxArea(vector<int> &height) {
      int m = 0;
      for (int l=0,r=height.size()-1; l<r; ) {
          int minHeight = height[l]<height[r]?height[l++]:height[r--];
          int area  = (r-l+1)*minHeight; // 注意这里要+1，因为上一句减1
          if (m < area) {
              m=area;
          }
      }
      return m;

  }
};
