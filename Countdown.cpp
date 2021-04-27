//Name: Ashok Surujdeo
//Email: Ashok.Surujdeo65@myhunter.cuny.edu
//This program runs: Countdown

#include <iostream>
using namespace std;

int main()
{
    int n;
    string word;
    cout << "Please enter a number: ";
    cin >> n;
    cout << "Please type a word: ";
    cin >> word;
    for (int i=n; i>0; i--)
    {
        cout << i << ", "; 
    }
    cout << "\n" << word;
    return 0;
}