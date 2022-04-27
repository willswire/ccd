#include <gmock/gmock.h>
#include "TestCode.h"

#define SIZE 10


TEST(MakeSentence_Tests, sentenceCases)
{
    char *sentence = makeSentence("TheQuickBrownFoxJumpedOverTheLazyDog'sBack");
    ASSERT_EQ(0, strcmp("The quick brown fox jumped over the lazy dog's back.", sentence));
    free(sentence);
    sentence = makeSentence("WhoIsTheMan");
    ASSERT_EQ(0, strcmp("Who is the man?", sentence));
    free(sentence);
    sentence = makeSentence("WilliamIsTheSoCalledPrince");
    ASSERT_EQ(0, strcmp("William is the so called prince.", sentence));
    free(sentence);
    sentence = makeSentence("WhatIsYourName");
    ASSERT_EQ(0, strcmp("What is your name?", sentence));
    free(sentence);
    sentence = makeSentence("HowDidYouDoThat");
    ASSERT_EQ(0, strcmp("How did you do that?", sentence));
    free(sentence);
    sentence = makeSentence("WhistleWhileYouWork");
    ASSERT_EQ(0, strcmp("Whistle while you work.", sentence));
    free(sentence);
    sentence = makeSentence("WhyIsThisAQuestion");
    ASSERT_EQ(0, strcmp("Why is this a question?", sentence));
    free(sentence);
    sentence = makeSentence("ILoveCProgrammingProblems");
    ASSERT_EQ(0, strcmp("I love c programming problems.", sentence));
    free(sentence);
    sentence = makeSentence("WhereIsWaldo");
    ASSERT_EQ(0, strcmp("Where is waldo?", sentence));
    free(sentence);
    sentence = makeSentence("WhenWillThisEverEnd");
    ASSERT_EQ(0, strcmp("When will this ever end?", sentence));
    free(sentence);
}
