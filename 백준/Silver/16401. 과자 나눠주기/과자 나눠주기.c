#include<stdio.h>
#define int long long

int n,m;
int arr[1010101];

int check(int x){
	int ret = 0;
	for (int i = 0; i < m; i++){
		ret += arr[i]/x;
	}
	return ret >= n;
}

signed main(){
	scanf("%lld %lld", &n, &m);
	for (int i = 0; i < m; i++) scanf("%lld", &arr[i]);
	
	int left = 0;
	int right = 1e18;
	
	while (left + 1 < right){
		int mid = (left+right)/2;
		
		if (check(mid)) left = mid;
		else right = mid;
	}
	
	printf("%lld", left);
	return 0;
}