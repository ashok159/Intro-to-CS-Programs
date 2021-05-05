//Name: Ashok Surujdeo
//Email: Ashok.Surujdeo65@myhunter.cuny.edu
//This program runs: Savings

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double amount, initialAmount;
    cout << "Please enter the starting amount: ";
    cin >> amount;
    initialAmount = amount;
    int i = 0;
    while (amount - initialAmount <= 1000)
    {
        if (i < 5)
        {
            amount *= 1.05;
        }
        else
        {
            amount *= 1.10;
        }
        cout << "Year " << (i+1) << " " << setprecision(2) << fixed << amount << endl;
        i++;
    }
    return 0;
}