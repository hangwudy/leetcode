//
// Created by hangwu on 1/3/22.
//

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        vector<string> week{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
        vector<int> monthDays{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int days = 365 * (year - 1971) + (year - 1969) / 4;
        for (int i = 0; i < month - 1; ++i) {
            days += monthDays[i];
        }
        if ((year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) && month >= 3) {
            days += 1;
        }
        days += day;
        return week[(days + 3) % 7];
    }
};

int main() {
    Solution solution;
    int d = 31, m = 8, y = 2019;
    string out = solution.dayOfTheWeek(d, m, y);
    cout << out << endl;
    return 0;
}