//
// Created by hangwu on 2021/11/8.
//
#include <string>
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    string getHint(string secret, string guess) {
        int bulls = 0;
        vector<int> sl(10), gl(10);
        for (int i = 0; i < secret.size(); ++i) {
            if (secret[i] == guess[i]) {
                bulls++;
            } else {
                sl[secret[i] - '0']++;
                gl[guess[i] - '0']++;
            }
        }
        int cows = 0;
        for (int i = 0; i < sl.size(); ++i) {
            cows += min(sl[i], gl[i]);
        }
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};


int main() {
    Solution solution;
    string secret = "1807", guess = "7810";
    string res = solution.getHint(secret, guess);
    cout << res << endl;
    return 0;
}