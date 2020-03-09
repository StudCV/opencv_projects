// ConsoleApplication1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <math.h>
using namespace std;

bool IsPointInArea(double x, double y) {
	return ((((x + 1) * (x + 1) + (y - 1) * (y - 1) >= 4) && y + x <= 0 && y - 2 * x <= 2)
		|| (((x + 1) * (x + 1) + (y - 1) * (y - 1) <= 4) && y + x >= 0 && y - 2 * x >= 2);
}
int main() {
	double x, y;
	cin >> x >> y;
	if (IsPointInArea(x, y)) cout << "YES";
	else cout << "NO";
	return 0;
}