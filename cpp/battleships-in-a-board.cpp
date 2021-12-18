//
// Created by hangwu on 12/18/21.
//
#include <vector>

using namespace std;

class Solution {
public:
    int countBattleships(vector<vector<char>> &board) {
        int row = board.size();
        int col = board[0].size();
        int ans = 0;

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (board[i][j] == 'X') {
                    board[i][j] = '.';
                    for (int m = i + 1; m < row && board[m][j] == 'X'; ++m) {
                        board[m][j] = '.';
                    }
                    for (int n = j + 1; n < col && board[i][n] == 'X'; ++n) {
                        board[i][n] = '.';
                    }
                    ans++;
                }
            }
        }
        return ans;
    }
};