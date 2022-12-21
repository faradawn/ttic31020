# Nice Advent of Code Repositories

## AOC Solution Repo
- [Reddit](https://www.reddit.com/r/adventofcode/)
- [C++ | split string and clock](https://github.com/rogue-kitten/aoc-22/blob/main/Days/Day15/part2.cpp)
- [Python | Borja](https://github.com/borjasotomayor/advent-of-code/blob/main/2022/day15.py)
- [Java | Sam Zheng](https://github.com/zd88884096/Advent-of-Code/tree/main/AOC-2022)
- [Python | Loren](https://github.com/LatCat1/advent-of-code/tree/master/2022)

## Tips
- Compile `g++ -Wall -std=c++17 day20.cpp; ./a.out`
- Read input by space: `cin >> s1 >> s2 >> s3`;
- Make integer long: `1L`
- Equation solver: [Mathpapa.com](https://www.mathpapa.com/simplify-calculator/)


## C++


- Set print precision
```c++
cout.precision(18);
cout << (double) 20753680468292344 / (double) 5577;
```


- Clock
```c++
auto start_clock = chrono::high_resolution_clock::now();
auto clock_duration = chrono::duration_cast<chrono::milliseconds>(chrono::high_resolution_clock::now() - start_clock);
cout << "~~~ Execution Time: " << clock_duration.count() << " ms\n";
```

- String Stream
```c++
#include <sstream>
string myline;
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


- Print matrix
```c++
void print_matrix(vector<vector<int>> &matrix){
    cout <<"--- printing matrix" << endl;
    for(auto& vec : matrix){
        for(auto &i : vec) cout << i << " ";
        cout << endl;
    }
    cout <<"--- done print matrix" << endl;
}

void print_vec(vector<int> &vec){
    for(int i : vec) cout << i << " ";
    cout << endl;
}
```