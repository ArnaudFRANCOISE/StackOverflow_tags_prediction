# Welcome to the StackOverflow tags prediction project!

During our last year as engineering student in artificial intelligence, we have been asked to develop a natural language processing solution to predict stackoverflow tags.  
In order to study stackoverflow question and to predict tags we will be using Random Forest and RNN.


# Files

All csv files has been downloaded thanks to SQL request on the StackOverflow database.
They has been stored inside the `/QueryResults` directory.
We aimed to classify **26 stackoverflow most popular tags.** We extracted about **10.000 corpus per tags.**
*(Unfortunately we had to really shortened our dataset due to limited computation power)*
## Data Preparation

A sum up of the preprocessing done is in the `data_analysis.ipynb` notebook.
For both model we had to clean the corpus:
	- Removing html balise
	- Removing stopword
	- Tokenization
	- Lemmatisation
	- Stemming
This has been applied to the whole corpus inside the `Top10_data_preparation`
# Random Forest
For the random forest once the corpus was cleaned we compute the tf-idf for each word. `RandomForest_tf-idf.ipynb`
We have only reached a **40% accuracy rate** we did not keep this pipeline.
*However with a biggest dataset we may reach about **80% accuracy rate***
# RNN

For the RNN pipeline we used the `keras.tonkenize.word_to_sequence` method to vectorize all word inside the corpus.
However we realised that the RNN training was really time consuming so we decided to only take 4000 features and 100 corpus per tags. 
We considered the TOP 10 stackoverflow tags:

    target_interest  = ["<c#>", "<c++>", "<java>", "<javascript>", "<html>","<css>","<android>",
                        "<python>", "<r>", "<sql>"]
Once the RNN trained, we reached a **0.89 validation accuracy rate** which is quite good considering the small dataset.

## Predictions

Here is a simple analysis of our prediction. 

![alt text](https://github.com/ArnaudFRANCOISE/StackOverflow_tags_prediction/blob/fea39a8f4c38a7e9539591b9d3c7a66f1c254376/RNN_model/Accuracy.png?raw=true)
The model prediction are quite difficult to clean as we have sometimes low probalities for each class.

    array([[0.50160116, 0.04523362, 0.0265328 , ..., 0.02360279, 0.00452808,
        0.02240554],
       [0.10306573, 0.24288872, 0.01265746, ..., 0.00849207, 0.08007599,
        0.03257773],
       [0.00874289, 0.02098964, 0.00135328, ..., 0.03234525, 0.02181898,
        0.01449805],
       ...,
       [0.01351722, 0.08484412, 0.00760453, ..., 0.01077135, 0.03770273,
        0.8511029 ],
       [0.01091659, 0.0326408 , 0.00486266, ..., 0.03158519, 0.05359608,
        0.01755047],
       [0.0101714 , 0.00773121, 0.00615104, ..., 0.08850229, 0.0353671 ,
        0.00311306]], dtype=float32)

After cleaning we reached a real **84% mean accuracy**.
