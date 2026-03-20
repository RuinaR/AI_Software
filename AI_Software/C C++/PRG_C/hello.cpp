#include <iostream>
using namespace std;

int main()
{

    int nInputData1 = 0;
    int nInputData2 = 0;
    int nSum = 0;

    cout << "첫 번째 숫자 입력 : ";
    cin >> nInputData1;

    cout << "두 번째 숫자 입력 : ";
    cin >> nInputData2;

    nSum = nInputData1 + nInputData2;
    cout << "두 숫자의 합 : " << nSum << endl;
    
    return 0;
}
