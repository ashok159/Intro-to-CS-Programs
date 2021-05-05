//Name: Ashok Surujdeo
//Email: Ashok.Surujdeo65@myhunter.cuny.edu
//This program runs: Letter Grade

#include <iostream>
using namespace std;

int main()
{
    float grade;
    cout << "Enter your grade: ";
    cin >> grade;
    if (grade < 60)
    {
        cout << "Your letter grade is F\n";
    }
    else if (60 <= grade && grade <80)
    {
        cout << "Your letter grade is C or D\n";
    }
    else if (80 <=grade && grade<90)
    {
        cout << "Your letter grade is B\n";
    }
    else
    {
        cout << "Your letter grade is A\n";
    }
    return 0;
}