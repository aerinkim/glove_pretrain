#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define bufSize 1024

void read_file(float* W);

int main()
{
	float* W = new float[50];		
	read_file(W);

	for (int i = 0; i < 3; i++)
	{
		printf("%f\n", W[i]);
	}

	int j;
	scanf("%d",&j);
}

void read_file(float *W)
{
	printf("You embedding is being opened...\n");
	FILE *fp;
	
	//if ((fp = fopen("C:\\GitHub\\base\\numerical\\c\\ReadFile1\\Debug\\data.txt", "r")) == NULL)
	
	// This is the W matrix. rows*columns
	//float W[30] = { 0.0 };
	//float *W = malloc(sizeof(float) * 50);

	int i = 0;

	// In this file, one row should contain only one NUMBER!!
	// So flatten your matrix.
	if (fp = fopen("C:\\GitHub\\base\\numerical\\c\\ReadFile1\\Debug\\data.txt", "r")) {
		while (fscanf(fp, "%f", &W[i]) != EOF) {
			++i;
		}
		fclose(fp);
	}

	for (--i; i >= 0; --i)
		printf("W[%d] = %f\n", i, W[i]);

	fclose(fp);

	scanf("%d",&i);    
}
