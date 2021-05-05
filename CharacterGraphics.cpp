//Name: Ashok Surujdeo
//Email: Ashok.Surujdeo65@myhunter.cuny.edu
//This program runs: Character Graphics

#include <iostream>
using namespace std;

int main()
{
    int n;
    string c;
    cout << "Please enter a number: ";
    cin >> n;
    cout << "Please enter a character: ";
    cin >> c;
    for (int i=1; i <=n; i++)
    {
        for (int j=1; j<=i; j++)
        {
            cout << c;
        }
        cout << endl;
    }
    for (int i=n-1; i>=1; i--)
    {
        for (int j=i; j>0; j--)
        {
            cout << c;
        }
        cout << endl;
    }
    return 0;
}