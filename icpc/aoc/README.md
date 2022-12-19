# Nice Advent of Code Repositories

## C++ Repo
- [C++, split string and clock](https://github.com/rogue-kitten/aoc-22/blob/main/Days/Day15/part2.cpp)
- [Python, Borja](https://github.com/borjasotomayor/advent-of-code/blob/main/2022/day15.py)

## Tips
- read input split string: cin >> s1 >> s2 >> s3;
- make integer long: 1ll, 1l


## C++
- String Stream
```c++
#include <sstream>
std::istringstream strm(myline);

```


- Split String
```c++
vector<string> split_str(string s, string delimiter){
    vector<string> res;
    int last = 0;
    int next = 0;
    while ((next = s.find(delimiter, last)) != string::npos) {
        res.push_back(s.substr(last, next-last));
        last = next + 1;
    }
    string last_str = s.substr(last, s.length()-last);
    res.push_back(last_str);
    return res;
}
```


- Print Matrix
```c++
void print_matrix(vector<vector<int>> &matrix){
    cout <<"--- printing matrix" << endl;
    for(auto& vec : matrix){
        for(auto &i : vec){
            cout << i << " ";
        }
        cout << endl;
        cout <<"--- done print matrix" << endl;
    }
}
```