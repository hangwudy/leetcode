//
// Created by hangwu on 10/20/21.
//
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    int minMoves(vector<int> &nums) {
        int minVal = *min_element(nums.begin(), nums.end());
        int res = 0;
        for (int num: nums) {
            res += num - minVal;
        }
        return res;
    }
};