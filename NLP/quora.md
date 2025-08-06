# Quora :: Repeated question but different answers problem - Semantically Duplicate Questions (i.e., different wording but same meaning)

## Data Acquisition 
1. From where would you acquire the data?
Ans. I will try to scrap the quora website.


## Text Preparation
1. What kind of cleaning steps would you perform?
Ans. Spelling mistakes, emojis removal, special characters removal, to lowercase

2. What text preprocessing step would you apply?
Ans. Tokenization, Stemming

3. Is advanced text preprocessing required?
Ans. According to me, Yes few like: POS tagging and coreference resolution


## Feature Engineering
1. What kind of features would you create? 
Ans. WordNet to check if words are synonyms


## Modelling
1. What algorithm would you use to solve the problem at hand?
Ans. Logistic Regression, Random Forest

2. What intrinsic evaluation metrics would you use?
Ans. Accuracy, Precision, Recall, and F1-score

3. What extrinsic evaluation metrics would you use?
Ans. Old system vs. new system, Increase in meaningful answers per unique question


## Deployment
1. How would you deploy your solution into the entire product?
Ans. In the form of API so that quora can use it

2. How and what things will you monitor?
Ans. Decrement in the duplicate questions, API latency

3. What would be your model update strategy?
Ans. Live changes according to the feedback from the users