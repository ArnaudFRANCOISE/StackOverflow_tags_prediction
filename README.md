# Welcome to the StackOverflow tags prediction project!

During our last year as engineering student in artificial intelligence, we have been asked to develop a natural language processing solution to predict stackoverflow tags.  
In order to study stackoverflow question and to predict tags we will be using Random Forest and RNN.


# Dataset

All csv files has been downloaded thanks to SQL request on the StackOverflow database. (https://data.stackexchange.com/stackoverflow/query/new)
They has been stored inside the `/QueryResults` directory.
We aimed to classify **26 stackoverflow most popular tags.** We extracted about **10.000 corpus per tags.**
*(Unfortunately we had to really shortened our dataset due to limited computation power)*
## Data Preparation

A sum up of the preprocessing done is in the `data_analysis.ipynb` notebook.
For both model we had to clean the corpus:
</br>	- Removing html balise
</br>	- Removing stopword
</br>	- Tokenization
</br>	- Lemmatisation
</br>	- Stemming
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
                      
The preparation of the RNN model follow this notebook execution order:

PART_I_TOP10_data_contraction.ipynb
PART_II_TOP10_StackOverflow_LSTM_corpus_contraction.ipynb
PART_III_TOP10_RNN_model_v1.ipynb

*(The preparation has been splitted because we first worked on google colab and experienced some RAM issues. The last notebooks (training of the RNN) has been mad locally thanks to Cuda and tensorflow-gpu installation in my python environment)*
    

Once the RNN trained, we reached a **0.84 validation accuracy rate** which is quite good considering the small dataset.

## Predictions

Here is a simple analysis of our prediction. 

![alt text](https://github.com/ArnaudFRANCOISE/StackOverflow_tags_prediction/blob/fea39a8f4c38a7e9539591b9d3c7a66f1c254376/RNN_model/Accuracy.png?raw=true)
The model prediction are quite difficult to clean as we have sometimes low probalities for each class.


After cleaning we reached a real **84% mean accuracy**.

# Website API
We also made an simple website with the **Flask** framework with python.
before running it make sure to run :

    #StackOverflow_tags_prediction/MyFlaskWebsite/MyFlaskWebsite
    pip install -r requirements.txt

Then with all modules installed, you can juste execute:

    #StackOverflow_tags_prediction/MyFlaskWebsite/MyFlaskWebsite
    main.py

