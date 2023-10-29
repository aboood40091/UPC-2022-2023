
#include <iostream>
#include <iomanip>
#include<bitset>
#include<string>
#include <set>
#include <queue>
using namespace std;

void print_queue(std::queue<pair<int,int>> q)
{
  while (!q.empty())
  {
    std::cout << q.front().first << ", " << q.front().second << endl;
    q.pop();
  }
  std::cout << std::endl;
}

pair<int,int> moves_sk[] = {
    make_pair(2,1), make_pair(2,-1),
    make_pair(-2,1), make_pair(-2,-1), 
    make_pair(1,2), make_pair(1,-2),
    make_pair(-1,2), make_pair(-1,-2),
    make_pair(2,2), make_pair(2,-2),
    make_pair(-2,2), make_pair(-2,-2)
    
};

pair<int,int> moves_k[] = {
    make_pair(2,1), make_pair(2,-1),
    make_pair(-2,1), make_pair(-2,-1), 
    make_pair(1,2), make_pair(1,-2),
    make_pair(-1,2), make_pair(-1,-2),
    
};

int solve_sk(pair<int,int> s_p, pair<int,int> e_p, int arr[][8]){
    
    queue<pair<int,int>> Q;
    Q.push(s_p);
    int count=1;
    while(!Q.empty()){
        int n = Q.size();
        for(int j=0; j<n; j++){
            pair<int,int> p = Q.front();
            Q.pop();
            for(int i=0 ; i<12; i++){
                int x, y;
                x = p.first + moves_sk[i].first;
                y = p.second + moves_sk[i].second;
                
                if(7<x || x<0 || 7<y || y<0 || arr[x][y] == -1) continue;
                if(arr[x][y] == 1){
                    return count;
                } 
                arr[x][y] = -1;
                Q.push(make_pair(x,y));
                
            }
        }
        count++;
    }
    return -1;
}

int solve_k(pair<int,int> s_p, pair<int,int> e_p, int arr[][8]){
    
    queue<pair<int,int>> Q;
    Q.push(s_p);
    int count=1;
    while(!Q.empty()){
        int n = Q.size();
        for(int j=0; j<n; j++){
            pair<int,int> p = Q.front();
            Q.pop();
            for(int i=0 ; i<8; i++){
                int x, y;
                x = p.first + moves_k[i].first;
                y = p.second + moves_k[i].second;
                
                if(7<x || x<0 || 7<y || y<0 || arr[x][y] == -1) continue;
                if(arr[x][y] == 1) return count;
                arr[x][y] = -1;
                Q.push(make_pair(x,y));
                
            }
        }
        count++;
    }
    return -1;
}

int main()
{
    int n;
    cin >>n;
    while(n--){
        int arr[8][8]= {};
        
        pair<int,int> start_p, end_p; 
        cin >>start_p.first >> start_p.second;
        start_p.second--;
        start_p.first--;
        cin >>end_p.first >> end_p.second;
        end_p.first--;
        end_p.second--;
        arr[start_p.first][start_p.second] = -1;
        arr[end_p.first][end_p.second] = 1;
        
        pair<int,int> temp;
        cin>>temp.first >> temp.second;
        while(temp.first != -1){
            arr[temp.first-1][temp.second-1] = -1;
            cin>>temp.first >> temp.second;
        }
        int arr2[8][8];
        for(int i=0; i<8; i++)
            for(int j=0; j<8; j++)
                arr2[i][j] = arr[i][j];
        cout  << solve_k(start_p, end_p, arr2)<<  " " <<solve_sk(start_p, end_p, arr) << endl;
        
        
        
    }
    return 0;
}