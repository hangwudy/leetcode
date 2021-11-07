//
// Created by hangwu on 10/13/21.
//
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        for (int i = 1; i < n + 1; ++i) {
            if (i % 3 == 0 && i % 5 == 0) {
                res.push_back("FizzBuzz");
            } else if (i % 3 == 0) {
                res.push_back("Fizz");
            } else if (i % 5 == 0) {
                res.push_back("Buzz");
            } else {
                res.push_back(to_string(i));
            }
        }
        return res;
    }
};

//int main() {
//    Solution so;
//    vector<string> res = so.fizzBuzz(15);
//    for (auto item: res) {
//        cout << item << endl;
//    }
//}