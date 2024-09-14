#include<iostream>
#include<vector>
using namespace std;
vector<int> merge(vector<int> arr1, vector<int> arr2){
    for (int i=0; i<arr2.size(); i++){
        arr1.push_back(arr2[i]);
    }
    return arr1;
}
int main(){
    vector<int> arr1={1,2,3,4};
    vector<int> arr2={5,6,7,8};
    vector<int> result=merge(arr1,arr2);
    for (int num : result){
        cout<<num<<" ";
    }
    cout<<endl;
    return 0;
    //This is demo
}