//Name: Ashok Surujdeo
//Email: Ashok.Surujdeo65@myhunter.cuny.edu
//This program runs: Two's Complement

#include <iostream>
using  namespace std;

int main()
{
    int n,b,x;
    cout << "Enter a number: ";
    cin >> n;
    if (n < 0)
    {
      cout << "1";
      x = 32 + n;
    }
    else
    {
      cout << "0";
      x = n;
    }
    b = 16;
    while (b > .5)
    {
      if (x >= b)
      {
        cout << "1";
      }
      else 
      {
        cout << "0";
      }
      x = x % b;
      b = b/2;
    }
    cout << "\n";
    return 0;
}