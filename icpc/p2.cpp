#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>

using namespace std;

int main(){
    int n;
    char c;
    cin >> n;
    queue<int> q;
    vector<int>vec(n);
    for(int i = 0; i < n; i++){
        cin >> c;
        if(c == 'Z'){
            vec[i] = 1;
        }else{
            vec[i] = 0;
        }
    }

    for(int i = n-1; i >= 0; i--){
        if(vec[i] == 0){
            q.push(n-1 - i);
        }
    }

    int time = 0;
    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int i = 0; i < cur; i++){
            q.push(i);
        }
        time ++;
    }

    cout << time << endl;

}