//Name: Ashok Surujdeo
//Email: Ashok.Surujdeo65@myhunter.cuny.edu
//This program runs: Inches to Feet

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float inches, feet;
    cout << "Please enter a length in inches: ";
    cin >> inches;
    feet = inches / 12;
    if (feet == 0.0)
    {
        cout << "The length is " << fixed << setprecision(0) << feet << " ft.";
    }
    else
    {
        feet = (int)(feet*100);
        feet = feet/100;
        cout << "The length is " << fixed << setprecision(2) << feet << " ft.";    
    }
    return 0;
}