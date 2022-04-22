#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// Refer to README.md for the problem instructions

char *checkAmount(double amount)
{
    int total = (int) 100 * (amount + 0.005);

    if (total <= 0 || total >= 10000) {
        return NULL;
    }

    const char ZERO[] = "ZERO";
    const char ONE[] = "ONE";
    const char TWO[] = "TWO";
    const char THREE[] = "THREE";
    const char FOUR[] = "FOUR";
    const char FIVE[] = "FIVE";
    const char SIX[] = "SIX";
    const char SEVEN[] = "SEVEN";
    const char EIGHT[] = "EIGHT";
    const char NINE[] = "NINE";
    const char TEN[] = "TEN";
    const char ELEVEN[] = "ELEVEN";
    const char TWELVE[] = "TWELVE";
    const char THIRTEEN[] = "THIRTEEN";
    const char FOURTEEN[] = "FOURTEEN";
    const char FIFTEEN[] = "FIFTEEN";
    const char SIXTEEN[] = "SIXTEEN";
    const char SEVENTEEN[] = "SEVENTEEN";
    const char EIGHTEEN[] = "EIGHTEEN";
    const char NINETEEN[] = "NINETEEN";
    const char TWENTY[] = "TWENTY";
    const char THIRTY[] = "THIRTY";
    const char FOURTY[] = "FORTY";
    const char FIFTY[] = "FIFTY";
    const char SIXTY[] = "SIXTY";
    const char SEVENTY[] = "SEVENTY";
    const char EIGHTY[] = "EIGHTY";
    const char NINETY[] = "NINETY";

    int doTensb = 0;
    char* tensa = calloc(sizeof(char), 50);
    if (total / 100) {
        switch (total / 100) {
            case 1:
                tensa = ONE;
                break;
            case 2:
                tensa = TWO;
                break;
            case 3:
                tensa = THREE;
                break;
            case 4:
                tensa = FOUR;
                break;
            case 5:
                tensa = FIVE;
                break;
            case 6:
                tensa = SIX;
                break;
            case 7:
                tensa = SEVEN;
                break;
            case 8:
                tensa = EIGHT;
                break;
            case 9:
                tensa = NINE;
                break;
            case 10:
                tensa = TEN;
                break;
            case 11:
                tensa = ELEVEN;
                break;
            case 12:
                tensa = TWELVE;
                break;
            case 13:
                tensa = THIRTEEN;
                break;
            case 14:
                tensa = FOURTEEN;
                break;
            case 15:
                tensa = FIFTEEN;
                break;
            case 16:
                tensa = SIXTEEN;
                break;
            case 17:
                tensa = SEVENTEEN;
                break;
            case 18:
                tensa = EIGHTEEN;
                break;
            case 19:
                tensa = NINETEEN;
                break;
            case 20:
                tensa = TWENTY;
                break;
            case 21 ... 29:
                tensa = TWENTY;
                doTensb = 1;
                break;
            case 30:
                tensa = THIRTY;
                break;
            case 31 ... 39:
                tensa = THIRTY;
                doTensb = 1;
                break;
            case 40:
                tensa = FOURTY;
                break;
            case 41 ... 49:
                tensa = FOURTY;
                doTensb = 1;
                break;
            case 50:
                tensa = FIFTY;
                break;
            case 51 ... 59:
                tensa = FIFTY;
                doTensb = 1;
                break;
            case 60:
                tensa = SIXTY;
                break;
            case 61 ... 69:
                tensa = SIXTY;
                doTensb = 1;
                break;
            case 70:
                tensa = SEVENTY;
                break;
            case 71 ... 79:
                tensa = SEVENTY;
                doTensb = 1;
                break;
            case 80:
                tensa = EIGHTY;
                break;
            case 81 ... 89:
                tensa = EIGHTY;
                doTensb = 1;
                break;
            case 90:
                tensa = NINETY;
                break;
            case 91 ... 99:
                tensa = NINETY;
                doTensb = 1;
                break;
            default:
                break;
        }
    } else {
        tensa = ZERO;
    }

    char* tensb = calloc(sizeof(char), 50);
    if (doTensb) {
        switch ((total / 100) % 10) {
            case 1:
                tensb = ONE;
                break;
            case 2:
                tensb = TWO;
                break;
            case 3:
                tensb = THREE;
                break;
            case 4:
                tensb = FOUR;
                break;
            case 5:
                tensb = FIVE;
                break;
            case 6:
                tensb = SIX;
                break;
            case 7:
                tensb = SEVEN;
                break;
            case 8:
                tensb = EIGHT;
                break;
            case 9:
                tensb = NINE;
                break;
            default:
                break;
        }
       strcat(tensa, " ");
       strcat(tensa, tensb);
    }
    
    char* checkValueInWords = calloc(sizeof(char), 100);
    sprintf(checkValueInWords, "%s and %i/100", tensa, (total % 100));

    return checkValueInWords;
}
