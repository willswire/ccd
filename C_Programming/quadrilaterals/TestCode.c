#include <stdio.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

void classify_quads(int quads[][4], int rows, struct QuadStruct *qds)
{
    qds->invalid = 0;
    qds->para = 0;
    qds->quad = 0;
    qds->rect = 0;

    for(int i = 0; i < rows; i++) {
        int angleA = quads[i][0];
        int angleB = quads[i][1];
        int angleC = quads[i][2];
        int angleD = quads[i][3];

        if (angleA + angleB + angleC + angleD != 360)
            qds->invalid += 1;
        else if (angleA * angleB * angleC * angleD <= 0)
            qds->invalid += 1;
        else if (angleA >= 360 || angleB >= 360 || angleC >= 360 || angleD >= 360)
            qds->invalid += 1;
        else if (angleA == angleB && angleB == angleC && angleC == angleD)
            qds->rect += 1;
        else if (angleA == angleC && angleB == angleD)
            qds->para += 1;
        else
            qds->quad += 1;
    }
}
