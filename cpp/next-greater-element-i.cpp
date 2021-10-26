//
// Created by hangwu on 2021/10/26.
//
#include <vector>
#include <unordered_map>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> hashmap;
        stack<int> stk;
        for (int i = nums2.size() - 1; i >= 0; --i) {
            while (!stk.empty() and nums2[i] >= stk.top()) {
                stk.pop();
            }
            hashmap[nums2[i]] = (stk.empty() ? -1 : stk.top());
            stk.push(nums2[i]);
        }
        vector<int> res;
        for (auto num: nums1) {
            res.emplace_back(hashmap[num]);
        }
        return res;
    }
};