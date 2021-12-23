//
// Created by hangwu on 12/20/21.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findRadius(vector<int> &houses, vector<int> &heaters) {
        int ans = 0;
        sort(heaters.begin(), heaters.end());
        for (int house: houses) {
            int j = upper_bound(heaters.begin(), heaters.end(), house) - heaters.begin();
            int i = j - 1;
            int rightDistance = j >= heaters.size() ? INT16_MAX : heaters[j] - house;
            int leftDistance = i < 0 ? INT16_MAX : house - heaters[i];
            int curDistance = min(leftDistance, rightDistance);
            ans = max(ans, curDistance);
        }
        return ans;
    }
};

int main() {
    Solution so;
    vector<int> houses = {1, 2, 3};
    vector<int> heaters = {2};
    int res = so.findRadius(houses, heaters);
    cout << res << endl;
    return 0;
}