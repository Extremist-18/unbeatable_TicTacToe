#include <bits/stdc++.h>
using namespace std;
#include "file.cpp"

map<string,int> mp;

int bestMove(char *a, char c){
    int best = INT_MIN;
    int move=-1;
    for(int i=0;i<9;i++){
        int curr=0;
        if(a[i]==' '){
            a[i] = c;
            curr = algorithm(a,0,true);
            if(curr >best){
                best = curr;
                move = i;
            }
            a[i] = ' ';
        }
    }

    return move;
}


int algorithm(char *a,int depth, bool isMaximizer){
    char *board = a;
    // if(checkTie(a))
    //     return tie;
    if(isMaximizer){
        int score = INT_MIN;

    }else{
        int score = INT_MAX;

    }
}

int main()
    {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    return 0;
    }