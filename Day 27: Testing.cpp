#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <cassert>
#include <set>

using namespace std;

int minimum_index(vector<int> seq) {
    if (seq.empty()) {
        throw invalid_argument("Cannot get the minimum value index from an empty sequence");
    }
    int min_idx = 0;
    for (int i = 1; i < seq.size(); ++i) {
        if (seq[i] < seq[min_idx]) {
            min_idx = i;
        }
    }
    return min_idx;
}
class TestDataEmptyArray{
public:
    static vector<int> get_array() { 
    //static is used to make the function independent of the object
    //get_array() can now be called without creating any object
        vector<int> arr{};
        return arr;
    }
};

class TestDataUniqueValues{
public:
    static vector<int> get_array() {
        vector<int> arr{3,2,4,1};
        return arr;
    }
    
    static int get_expected_result() {
        return 3;
        //3rd index contains the min value.
    }
};

class TestDataExactlyTwoDifferentMinimums{
public:
    static vector<int> get_array() { 
        vector<int> arr {2,2,1,1,3}; 
        // array with two more than 1 elements as min. 
        // First occurence of min element at 2nd index.
        return arr;
    }
    
    static int get_expected_result() {
        return 2; 
        // 2nd index i.e 3rd element of above array is the minimum.
    }
};

