#include <ctime>
#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vvc vector<vector<char>> 
char p ='X';
char c= 'O';

void drawBoard(vvc &a);
void player(vvc &a, char p);
void computer(vvc &a, char c);
int checkWin(vvc &a, char p);
int checkTie(vvc &a);
pair<int,int> bestMove(vvc &a, char c);
int algorithm(vvc &a,int depth, bool isMaximizer);

int main(){
    vector<vector<char>> a(3,vector<char>(3,' '));

    bool playing = true;
    drawBoard(a);

    while(playing){
        computer(a,c);
        drawBoard(a);
        int isWin = checkWin(a,p);

        if(isWin!=-1){
            if(isWin>0)
                cout<<"Congratulations! YOU WON!!";
            else
                cout<<"OOPS!! YOU LOSE! Try again!";
            // playing = false;
            break;
        }else if(checkTie(a)!=-1){
            cout<<"Its a TIE!!";
            // playing = false;
            break;
        }

        player(a,p);
        drawBoard(a);
        isWin = checkWin(a,p);
        if(isWin!=-1){
            if(isWin>0)
                cout<<"Congratulations! YOU WON!!";
            else
                cout<<"OOPS!! YOU LOSE! Try again!";
            // playing = false;
            break;
        }else if(checkTie(a)!=-1){
            cout<<"Its a TIE!!";
            // playing = false;
            break;
        }
    }
    return 0;
}

void drawBoard(vvc &arr){
    cout<<'\n';
    cout<<"     |     |     "<<'\n';
    cout<<"  "<<arr[0][0]<<"  |  "<<arr[0][1]<<"  |  "<<arr[0][2]<<'\n';
    cout<<"_____|_____|_____"<<'\n';
    cout<<"     |     |     "<<'\n';
    cout<<"  "<<arr[1][0]<<"  |  "<<arr[1][1]<<"  |  "<<arr[1][2]<<'\n';
    cout<<"_____|_____|_____"<<'\n';
    cout<<"     |     |     "<<'\n';
    cout<<"  "<<arr[2][0]<<"  |  "<<arr[2][1]<<"  |  "<<arr[2][2]<<'\n';
    cout<<"     |     |     "<<'\n';
    cout<<'\n';
}

void player(vector<vector<char>> &arr,char p){

    int r,c;
    do{
        cout<<" Choose your move(enter row nd col number(Not index)): ";
        cin>>r>>c;
        r--;c--;
        if(r>=0 && r<3 && c>=0 && c<3 && arr[r][c]==' '){
            arr[r][c] = p;
            break;
        }else{
            cout<<"Choose a valid move: \n";
            // break;
        }
    }while(r<0 || r>=3 || c>=3 || c<0 || arr[r][c]!=' ');
}

void computer(vector<vector<char>> &arr, char c){
    pair<int,int> p = bestMove(arr,c);
    arr[p.first][p.second] =c;
}

int checkWin(vvc &a, char x) {

    for (int i = 0; i < 3; i++) {
        if (a[i][0] != ' ' && a[i][0] == a[i][1] && a[i][0] == a[i][2]) {
            return (a[i][0] == x) ? 10 : -10;
        }
        if (a[0][i] != ' ' && a[0][i] == a[1][i] && a[0][i] == a[2][i]) {
            return (a[0][i] == x) ? 10 : -10;
        }
    }

    // diagonals
    if (a[0][0] != ' ' && a[0][0] == a[1][1] && a[0][0] == a[2][2]) {
        return (a[0][0] == x) ? 10 : -10;
    }
    if (a[0][2] != ' ' && a[0][2] == a[1][1] && a[0][2] == a[2][0]) {
        return (a[0][2] == x) ? 10 : -10;
    }

    return -1; 
}

int checkTie(vector<vector<char>> &a){
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(a[i][j]==' ')
                return -1;
        }
    }
    return 0;        
}

pair<int,int> bestMove(vector<vector<char>> &a, char c){
    int best = INT_MIN;
    pair<int,int> move={-1,-1};

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            int curr =0;
            if(a[i][j]==' '){
                a[i][j]=c;
                curr = algorithm(a,0,false);
                a[i][j] = ' ';

                if(curr >best){
                    best = curr;
                    move = {i,j};
                }
            }
        }
    }
    return move;
}

int algorithm(vector<vector<char>> &a,int depth, bool isMaximizer){
    vector<vector<char>> board = a;
    // int isWin = isMaximizer ? checkWin(board, c) : checkWin(board, p);
    int isWin = checkWin(a, isMaximizer ? c : p);
    if(isWin!=-1){
        if(isWin>0)
            return isWin-depth;
        else
            return isWin +depth;    
    }
  
    if(checkTie(board)!=-1)
        return 0;

    if(isMaximizer){
        int best_mx = INT_MIN;

        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(board[i][j]==' '){
                    board[i][j]=c;    // may be i should pass variable for player as well. think this
                    int score = algorithm(board,depth+1,false);
                    board[i][j]=' ';
                    best_mx = max(best_mx,score);
                }
            }
        }
        return best_mx-depth;

    }else{
        int best_mn = INT_MAX;

        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(board[i][j]==' '){
                    board[i][j]=p;    // may be i should pass variable for player as well. think this
                    int score = algorithm(board,depth+1,true);
                    board[i][j]=' ';
                    best_mn = min(best_mn,score);
                }
            }
        }
        return best_mn+depth;
    }


}
