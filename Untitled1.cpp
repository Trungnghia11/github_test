#include<iostream>
using namespace std;
int luythua(int so,int mu){
	int kqua =1;
	for(int i = 1; i <= mu; i++)  {
        kqua = kqua * so;
    }
	return kqua;
}
int tinhmau(int x)
{
	int mau=0;
	for(int i=0;i<=x;i++)
	{
		mau+=i;
	}
	return mau;
}
int main()
{
	int n,x;
	float tong=0;
	int tu=1,mau=1;
	int dau = -1;
	cout<<"Nhap x:";
	cin>>x;
	cout<<"Nhap n:";
	cin>>n;

	for(int i = 1;i<=n;i++)
	{
		tu = luythua(x,i);
		mau = tinhmau(i);
		float phanso =(float)tu/mau;
		tong = tong + dau*phanso;	
		dau=(-1)*dau;
	}
	cout<<"Tong: "<<tong;
}
