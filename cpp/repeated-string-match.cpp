//
// Created by hangwu on 12/22/21.
//
#include <iostream>

using namespace std;

class Solution {
public:
    int strStr(string hayStack, string needle) {
        int n = hayStack.size();
        int m = needle.size();
        if (m == 0) {
            return 0;
        }
        long long k1 = 1e9 + 7;
        long long k2 = 1337;
        srand((unsigned) time(NULL));
        long long kMod1 = rand() % k1 + k1;
        long long kMod2 = rand() % k2 + k2;

        long long hash_needle = 0;
        for (auto c: needle) {
            hash_needle = (hash_needle * kMod2 + c) % kMod1;
        }
        long long hash_hayStack = 0, extra = 1;
        for (int i = 0; i < m - 1; i++) {
            hash_hayStack = (hash_hayStack * kMod2 + hayStack[i % n]) % kMod1;
            extra = (extra * kMod2) % kMod1;
        }
        for (int i = m - 1; (i - m + 1) < n; i++) {
            hash_hayStack = (hash_hayStack * kMod2 + hayStack[i % n]) % kMod1;
            if (hash_hayStack == hash_needle) {
                return i - m + 1;
            }
            hash_hayStack = (hash_hayStack - extra * hayStack[(i - m + 1) % n]) % kMod1;
            hash_hayStack = (hash_hayStack + kMod1) % kMod1;
        }
        return -1;
    }

    int repeatedStringMatch(string a, string b) {
        int an = a.size(), bn = b.size();
        int index = strStr(a, b);
        if (index == -1) {
            return -1;
        }
        if (an - index >= bn) {
            return 1;
        }
        return (bn + index - an - 1) / an + 2;
    }
};
