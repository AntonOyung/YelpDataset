# YelpDataset
Stat 198 Research

Research on the Yelp Academic 2017 dataset. Using LDA to analyze Yelp reviews. 

Goal:
Write a comprehensive summary of 1 restaurant based off of all the reviews

Process:
Separate all reviews for one restaurant by # stars
Run LDA on each review set
Analyze the distribution of ratings to determine the proportion of good and bad sentences
Using top topics/words in output find more representative sentence/review from the data
  (implemented ourselves or using a API)

Testing:
Manual checking
Check coherence

Ex. Output 

Restaurant
Mon Ami Gabi

Reviews 
{3.5: 0, 1: 188, 2: 362, 3: 755, 4: 2335, 5: 2774, 1.5: 0, 4.5: 0, 2.5: 0}

Topics 
[(0, '0.027*"breakfast" + 0.025*"egg" + 0.011*"benedict" + 0.010*"good" + 0.010*"brunch" +
    0.010*"toast" + 0.009*"coffe" + 0.008*"crepe" + 0.008*"waffl" + 0.008*"great"'),
  (1, '0.015*"chees" + 0.012*"salad" + 0.011*"goat" + 0.010*"great" + 0.009*"servic" +
    0.009*"seafood" + 0.008*"delici" + 0.008*"bread" + 0.008*"meal" + 0.008*"gluten"'),
  (2, '0.022*"great" + 0.021*"food" + 0.015*"vega" + 0.013*"good" + 0.013*"view" +
    0.013*"bellagio" + 0.012*"servic" + 0.011*"patio" + 0.011*"restaur" + 0.011*"fountain"'),
  (3, '0.019*"steak" + 0.014*"order" + 0.012*"good" + 0.009*"like" + 0.008*"french" +
    0.008*"frite" + 0.007*"sauc" + 0.007*"soup" + 0.007*"fri" + 0.007*"realli"'),
  (4, '0.016*"us" + 0.014*"tabl" + 0.011*"food" + 0.011*"wait" + 0.011*"order" +
    0.008*"minut" + 0.008*"reserv" + 0.008*"ask" + 0.008*"server" + 0.008*"seat"')]