#include <gmock/gmock.h>
#include "TestCode.h"
    
#define SIZE 16

TEST(Classify_quads_Tests, checkQuads)
{
    int quads[][4] = {{90,90,90,90},  //rect
                      {160,70,30, 100}, //quad
                      {110,70,10, 170},  //quad
                      {410,70,10, 170}, //invalid
                      {-10,90,110, 170}, //invalid
                      {100,100,100, 100}, //invalid
                      {110,70,110, 70}, //para
                      {100,70,120, 70}, //quad
                      {110,110,140,0}, //invalid
                      {110,110,0,140}, //invalid
                      {110,0,140,110}, //invalid
                      {0,110,140,110}, //invalid
                      {360,10,10,-20}, //invalid
                      {90,90,91,89}, //quad
                      {40, 140, 40, 140}, //para
                      {40, 130, 40, 150}, //quad
    };
    struct QuadStruct temp = { 0,0,0,0};
    classify_quads(quads, SIZE, &temp);
    ASSERT_EQ(temp.rect,1);
    ASSERT_EQ(temp.para,2);
    ASSERT_EQ(temp.quad,5);
    ASSERT_EQ(temp.invalid,8);

}

