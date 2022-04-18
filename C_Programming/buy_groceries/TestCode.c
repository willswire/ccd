#include <stdio.h>
#include <math.h>

// Refer to README.md for the problem instructions

int buyGroceries(int stuff[], int size)
{
    const float PRICE_EGGS = 3.50;
    const float PRICE_MILK = 2.25;
    const float PRICE_BREAD = 1.99;
    const float PRICE_SUGAR = 4.15;

    // Validate the given inputs
    if (size % 2 == 1 || size <= 0) {
        return 0;
    } else if (stuff == NULL) {
        return 0;
    }

    float total;
    int itemId;
    int itemQuantity;
    // Iterate through the list of stuff
    for (int i = 0; i < size; i++) {

        // The current number is the item id if its index is even
        if (i % 2 == 0) {
            itemId = stuff[i];
        // The current number is the item quantity if its index is odd
        } else {
            itemQuantity = stuff[i];
            if (itemQuantity <= 0) {
                return 0;
            }

            // Apply a discount for quantities greater than 
            float multiplier = itemQuantity < 5 ? itemQuantity : itemQuantity * 0.95;
            
            switch (itemId)
            {
            case 1:
                total += multiplier * PRICE_EGGS;
                break;
            case 2:
                total += multiplier * PRICE_MILK;
                break;
            case 3:
                total += multiplier * PRICE_BREAD;
                break;
            case 4:
                total += multiplier * PRICE_SUGAR;
                break;
            default:
                return 0;
            }
        }
    }
    return round(total);
}
