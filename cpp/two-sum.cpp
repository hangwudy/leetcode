//
// Created by hangwu on 2021/10/27.
//
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]);
            if (it!=hashtable.end()) {
                return {it->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 2, 4};
    int target = 6;
    vector<int> res = solution.twoSum(nums, target);
    for (auto a: res) {
        cout<<(a)<<" ";
    }
    cout<<endl;
}