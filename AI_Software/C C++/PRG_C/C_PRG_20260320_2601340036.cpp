#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    string strName = "";
    int nAge = 0;
    string strTarget = "";
    int nMaxTargetRatio = 0;
    int nCurrentTargetRatio = 0;
    bool bActive = false;
    float fTargetRatio = 0.0f;

    cout << "이름 입력 : ";
    cin >> strName;
    cout << "나이 입력 : ";
    cin >> nAge;
    cout << "목표 입력 : ";
    cin >> strTarget;
    cout << "목표 달성치 입력 : ";
    cin >> nMaxTargetRatio;
    cout << "현재 달성치 입력 : ";
    cin >> nCurrentTargetRatio;
    cout << "비전 활성화 여부 입력 (0 또는 1) : ";
    cin >> bActive;
    
    fTargetRatio = (float)nCurrentTargetRatio / (float)nMaxTargetRatio * 100.0f;

    cout << "이름 : " << strName << "(" << nAge << "세)" << endl;
    cout << "목표 비전 : " << strTarget << endl;
    cout << "진행도 : " << nCurrentTargetRatio << "/" << nMaxTargetRatio << endl;
    cout << "현재 달성률 : "<< fTargetRatio << "%" << endl;
    cout << "운영 상태 : " << (bActive ? "진행 중" : "준비 중") << endl;


    return 0;
}
