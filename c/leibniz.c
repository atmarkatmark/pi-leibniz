#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double leibniz(unsigned long long n)
{
	double sum = 0;

	/* iが偶数 */
	for (unsigned long long i = 0; i < n; i += 2)
		sum += 1.0 / (2 * i + 1);
	
	/* iが奇数 */
	for (unsigned long long i = 1; i < n; i += 2)
		sum += -1.0 / (2 * i + 1);
	
	return sum;
}

int main(int argc, char *argv[])
{
	clock_t start;
	int digit = 1;
	int times = 5;

	/* 桁数が指定されているか確認 */
	if (argc < 2)
	{
		puts("Usage: %s NUMBER_OF_DIGITS");
		return -1;
	}

	/* パラメータから桁数を取得 */
	digit = atoi(argv[1]);

	/* Leibnizの公式を計算 */
	start = clock();
	for (int i = 0; i != times; ++i)
		printf("pi: %.12lf\n", 4 * leibniz((unsigned long long )pow(10, digit)));
	printf("time: %.2lf\n", (clock() - start) * 1.0 / CLOCKS_PER_SEC / times);
	
	return 0;
}