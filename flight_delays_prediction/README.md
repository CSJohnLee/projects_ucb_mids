# Flight Delays Prediction (Machine Learning at Scale)  
A notebook (ran on Databricks) detailing the process of exploratory data analysis, data pre-processing, feature engineering, joining data, and training and tuning machine learning models. 
John's primary focus was on processing more than 30 million flights and 630 million weather raw data (including feature creations) into machine learning ready datasets.

#### Abstract
Flight delays cost airlines and passengers tens of billions of dollars each year. These costs can be mitigated by planning ahead for delays to avoid issues such as passengers missing connections or lower aircraft utilization. Therefore, we tackled this problem by answering the question: Given flight and weather information known two hours ahead of planned departure time, will a flight depart on time (within 15 minutes of scheduled departure) or will it be delayed or cancelled? In this notebook, we answered the question using machine learning with Spark, a large-scale data processing analytics engine, to handle the dataset of more than 30,000,000 rows. Our discussions include exploratory data analysis that guided feature engineering efforts. Additionally, we worked with and tuned different algorithms such as logistic regression, decision tree, random forest, and gradient boosted tree. Our final model was a tuned gradient boosted tree that utilized Principal Components Analysis (PCA) for dimensionality reduction. This model achieved an accuracy of 0.652 and an F1 score of 0.458.

#### Slide Deck:
W261 Fall2020 - Final Presentation - Team 25.pptx

#### Final Notebook:
W261_FA20_FINAL_PROJECT_TEAM25.ipynb

#### Supplemental Notebooks: 
Phase 1  - Full Flights Data - Processing and Storing to Database.ipynb  
Phase 1 - Weather Data - Processing and Storing to Database.ipynb  
Flight Data - Stage 2 - Ensure Airports Have Weather Data.ipynb  
Phase 2 - Flights & Weather Data - Join.ipynb  
Phase 3 - Train Split.ipynb  
Phase 3 - Validation&Test Split.ipynb  
Additional Modeling.ipynb  
