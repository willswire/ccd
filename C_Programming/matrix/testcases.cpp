#include <gmock/gmock.h>
#include "TestCode.h"


TEST(ProcessMatrix_Tests, normalCases)
{
    int stuff[5][5] = { {2,3,2,4,5},
                 {5,6,7,5,4},
                 {9,3,6,8,3},
                 {1,3,7,9,3},
                 {5,2,3,4,2} };

    int changedStuff[5][5] = { {4,3,4,4,10},
                             {5,3,7,2,4},
                             {18,3,12,8,6},
                             {1,1,7,4,3},
                             {10,2,6,4,4} };

    ASSERT_EQ(135, processMatrix(stuff, 5));

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            ASSERT_EQ(stuff[i][j], changedStuff[i][j]);
        }
    }

    int stuff2[8][5] = { {10,20,30,40,50},
                            {8,7,6,5,4},
                            {1,2,3,4,5},
                            {500,400,300,200,100},
                            {5,10,15,20,25},
                            {3,6,9,12,15},
                            {20,40,60,80,100},
                            {0,0,0,0,0} };
    

    int changedStuff2[8][5] = { {20,20,60,40,100},
                            {8,3,6,2,4},
                            {2,2,6,4,10},
                            {500,200,300,100,100},
                            {10,10,30,20,50},
                            {3,3,9,6,15},
                            {40,40,120,80,200},
                            {0,0,0,0,0} };

    ASSERT_EQ(2123, processMatrix(stuff2, 8));

    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            ASSERT_EQ(stuff2[i][j], changedStuff2[i][j]);
        }
    }
}
