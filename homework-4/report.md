# AI- HW 4:

## I. Bayesian Network Modeling

### Part 1

Search algorithm graph:

![Screen Shot 2018-04-06 at 5.17.15 PM](undirected.png)

Graph after I fix the undirected edges:

![directed](directed.png)

#### Answers:

1. ###### Explain, using the theory behind BN structures, why the search algorithm was able to orient some edges but not others. Reference the graph you found above.

   Because for both of this cases no sink is created or destroyed depending on the direction of the edge (only changes from fork to chain if it even changes), hence both directions of this edge make it equivalent.

2. ###### Explain your choices for network structure that you made above -- why did you orient the ambiguous edges the way that you did?

   I oriented `P -> I` because I assume that your opinion on immigration is an effect from your political inclination (just based on basic knowledge). Furthermore, since we have `P->D` being a similar issue to that of immigration then we need  `P -> I`  for the model to be consistent logically.

   I oriented `A->G` because it makes no sense that your position on gun control determines something about your age group.



### Part II
1. Probability that I win the campaing is of:` 37.3%`. My opponent is charted to win the congressional seat by a margin of roughly `25.4%` ( see exact results from script).

2. ###### In a small paragraph, argue for whether or not you believe this practice should be considered ethical, especially if each individual's characteristics were collected via social media. Compare this practice to targetted consumerist advertising wherein ads are curated based on perceived interests.

   I think it is ethical as long as the participants on the survey knew that their information (eventhough it is anonymous) was going to be released to the public. I personally think that there are pros and cons to machine learning and technology. Some people only want the pros, which are having all these cool services for free, but they don't realize that that comes to the cost that these firms are using your data to create such services. If you don't accept that then you shouldn't be using such services or answering surveys about your poitical affiliation. Now if they say these data was not going to be released to the public but then they do so anyways, then there I think it is not ethical. 

   In regards to comparison between consumerist addvertising, I feel like this is the exact same thing. Such ads work in the way that companies like Google or Facebook use your data to recommend you things you may like. I see no difference when it comes to political campaigns. As I mentioned before, if you are against one (aka political campaings using such informaiton) then you should be against all ML services.

##### RESULTS FOR BN:  (in the order that they were given):

```
1) P(V | A=1)
2) P(V | G=0)
3) P(V | G=0,I=0)
4) P(V | I=0,G=1)
5) P(V | A=0,P=1,I=0,D=0,G=0)
6) P(V | A=0,P=1,I=1,D=1,G=0)
7) P(V | A=1,P=0,I=0,D=0,G=1)
```

```
{'1': 0.35650000000000015, '0': 0.6434999999999998} -> Opponent wins -> TARGET
{'1': 0.31250000000000017, '0': 0.6875}             -> Opponent wins -> TARGET
{'1': 0.6999999999999998, '0': 0.3000000000000001}  -> I win -> DON'T TARGET
{'1': 0.5, '0': 0.5}                                -> 50/50 each -> TARGET (not priority)
{'1': 0.6999999999999998, '0': 0.3000000000000001}  ->  I win -> DON'T TARGET
{'1': 0.20000000000000015, '0': 0.7999999999999999} -> Opponent wins -> TARGET
{'1': 0.5, '0': 0.5}                                -> 50/50 each -> TARGET (not priority)
```

## II. Naive Bayes Classification (NBC)

##### RESULTS FOR BN:  (in the order that they were given):

```
{'1': 0.35650000000000015, '0': 0.6434999999999998} -> Opponent wins -> TARGET
{'1': 0.31250000000000017, '0': 0.6875}             -> Opponent wins -> TARGET
{'1': 0.6999999999999998, '0': 0.3000000000000001}  -> I win -> DON'T TARGET
{'1': 0.5, '0': 0.5}                                -> 50/50 each -> TARGET (not priority)
{'1': 0.6999999999999998, '0': 0.3000000000000001}  ->  I win -> DON'T TARGET
{'1': 0.20000000000000015, '0': 0.7999999999999999} -> Opponent wins -> TARGET
{'1': 0.5, '0': 0.5}                                -> 50/50 each -> TARGET (not priority)
```

##### RESULTS FOR NBC (in the order that they were given):

```
P(V | A=0,P=1,I=0,D=0,G=0)
P(V | A=0,P=1,I=1,D=1,G=0)
P(V | A=1,P=0,I=0,D=0,G=1)
```

```
     0           1
------------------------------------
[[0.46720151 0.53279849] -> I WIN  -> DON'T TARGET
 [0.73911226 0.26088774] -> I LOSE -> TARGET
 [0.36620794 0.63379206]] -> I WIN -> DON'T TARGET
```

1. ###### Between your BN and NBC, did any of your queries return different probability values? If so, explain why this difference is witnessed, and answer: which one will be more accurate for inference queries?

   All queries gave different probability values, though the last query is very similar for both. The reason for this is explained bellow.

   BN creates a better model in comparison to reality, hence it is more accurate.  NBC is called "naive" because it assumes independence on all features, hence less accurate. Furthermore, on NBC we label one variable the class variable, and all the rest are childrens of it. As a consequence  queries are really limited around that interpretation. Because of these two reasons, we see different probability values for our two models when tested on the same queries. Its important to mention that even though NBC is less accurate for inference queries it still succeeds in classifying and works good for smaller datasets.

2. ###### Are there some queries that your BN can answer out-of-the-box, once constructed, that your NBC cannot? If so, explain why this is the case and then list 3 such queries.

   Yes, queries such as the following:

   1) `P(A=1)`
   2) `P(I=0)`
   3) `P(D=1| P=1, A=1)`

   (Basically all queries that do not involve wanting to know something about V (the class variable)).

   This is because NBC  is not meant to answer general inference queries except those that pertain to classification.

3. ###### Between your BN and NBC, did any of your queries (despite possibly different probability values) provide a different determination for an individual's predicted voting predilection (V)? For example, did your BN say an individual with some features would vote for your opponent, but your NBC said that same individual would vote for your candidate? If there are differences, answer: which one should you follow if you want to maximize your canvassing efficacy? Provide some proof from the data to back up this claim, assuming that the data is representative of your congressional district.

   The first two agree, but the last one does not. Lets discuss this last query more in detail. As you can see BN shows us that there is a `50%` chance to lose and hence a `%50` change to lose. However, if you look at the results for NBC, it states that we win by `63%` . This means that NBC has a "stronger" opinion on targeting vs not targeting than that of BN.  However, if we look at the data we can see that for that specific query we get the following

   **query 3**

   1: 965 -> `50%`

   0: 969 -> `50%`

   This means that from the data we have that `50%` of the people with this query specifications will vote for me and `50%` will not. Hence, we can see how BN did a better job at modeling such inference query (since probability value relates more to reality). This might be because NBC is too simplified in the relationship model (same thing that we discussed on answer to 1).

4. ###### In a paragraph, make a comparative argument for the pros and cons of BNs vs. NBCs on both inference and classification tasks.

BN are necessary to perform general inference tasks, whereas NBC fails to perform them. This is because NBC can only make inference on probabilities regarding the class variable. Furthermore, NBC assumes independence between all features which might not be true in reality hence give worst results for inference queries. BN does not assume independence, hence turns out to be more representative of reality in some cases (because it can model these relationships). Also because of the model that NBC has, that is 1 variable being parent of all the rest, this makes it very limited to represent reality. It is important to note that BN has the overhead of using Tetrad, which is incovenient, however, this tool allows us to determine better relationships when there are a lot of variables.

On the other hand, eventhougn NBC may not be as accurate as BN in regards to inference queries, it is a simple and elegant model that still succeeds at classifying. NBC has the advantage that it depends solely on the data and it works well even for small datasets .

(Also refer to number one, more information is provided there)