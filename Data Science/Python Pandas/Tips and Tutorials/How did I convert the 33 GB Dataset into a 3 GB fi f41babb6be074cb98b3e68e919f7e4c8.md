# How did I convert the 33 GB Dataset into a 3 GB file Using Pandas? | by Arunkumar N | aatomz research | Sep, 2022 | Medium

[https://medium.com/aatomz-research/how-did-i-convert-the-33-gb-dataset-into-a-3-gb-file-using-pandas-b21d8da205c0](https://medium.com/aatomz-research/how-did-i-convert-the-33-gb-dataset-into-a-3-gb-file-using-pandas-b21d8da205c0)



credits to: aatomz

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1GpxIDx0Xa3DmftwmH1iQ0g.png](1GpxIDx0Xa3DmftwmH1iQ0g.png)

Optimizing the dataset memory is the first and critical step in any data science project. A dataset may contain thousand to millions of rows. We can load the smaller dataset quickly, but when the dataset gets bigger, our system may not be able to run the large memory files. So I thought to share how I converted the 33GB data file into 3GB for easy loading.

## Dataset

I have taken the recently trending ‘American Express-Default prediction’ dataset. You can download it from [Kaggle](https://www.kaggle.com/competitions/amex-default-prediction/data) for reproducibility.

## Importing the Libraries

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/18WY5hqGYAVnZYq9QBPMNvg.png](18WY5hqGYAVnZYq9QBPMNvg.png)

[Pandas](https://pandas.pydata.org/docs/getting_started/index.html) is one of the most commonly used libraries in python for data analysis. We can use it for data processing such as manipulation, concatenating, joining, merging, statistical analysis of data, and many more.

A garbage [collector(GC)](https://docs.python.org/3/library/gc.html) frees up the space from the memory while handling extensive data. It removes unwanted things from memory.

The glob module extracts specific files using patterns from our system.

OS module interacts with the operating system and handles the file and its paths.

## Chunking

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1sPHmIt6_KEkWHpt_42iN-w.png](1sPHmIt6_KEkWHpt_42iN-w.png)

Here we can’t be able to load the data file generally as we do in pandas since the file size is heavier, causing a memory error. So we use the ‘chunk size’ option to split the files as we wish. Here I have chosen 5 lakh rows per chunk. Here ‘GC.collect()’ is crucial and vital since it saves you from a memory error. I got 23 chips after running this.

After chunking, see whether you can read the chunk and check the info.

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1GF1bwFV1ukjRj1PNFyNGsg.png](1GF1bwFV1ukjRj1PNFyNGsg.png)

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1XuMsYjZrxoj5DVhpteIqPQ.png](1XuMsYjZrxoj5DVhpteIqPQ.png)

From the info, we can see that there are 190 columns with float64 in 185 columns. It is one of the common problems with Pandas always loading the float data as float64. By optimizing this memory, we could have reduced a part of the memory from our dataset. So we have to convert it to ‘float16’ or ‘float32’ to minimise memory usage. Here I have converted it to ‘float16’.

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1LAJpJNQifhMQ1CS3RH8HRg.png](1LAJpJNQifhMQ1CS3RH8HRg.png)

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1X8fc0hpVzpFKu-cj2gAGqQ.png](1X8fc0hpVzpFKu-cj2gAGqQ.png)

You can see after converting to ‘float16,’ memory usage has been drastically reduced.

## Optimizing and concatenating

Previously we read and optimized for a single chunk file. Now we are going to contact all 23 chunk files as well as optimize the memory.

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1iPq3idO_lxSn4HCAz2Q_6g.png](1iPq3idO_lxSn4HCAz2Q_6g.png)

Here I have used ‘glob’ and ‘ os. Path. join’ method to access corresponding files by file path and its component, i.e. (“*.csv”). We have to read all the files by iteration. During iteration, we can use conditions to convert from ‘float64’ to ‘float16’. After converting, we have to save the chunks in a list. Then we can contact all the files from the list and keep them in a new data frame.

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/13xw4k6FdpfUfXSb081dJpA.png](13xw4k6FdpfUfXSb081dJpA.png)

Now you can see the details of the new data frame after concatenating. We can do data processing operations in this data frame quickly. We can read 11 million rows at an instance, which is initially impossible due to the bigger file size.

## Converting data frame to file format

The optimized data frame could be converted into any file format. I recommend the feather format because of its lightweight, as you see below.

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1czBr8-QRBBdd4lbF3vbCxg.png](1czBr8-QRBBdd4lbF3vbCxg.png)

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1KoD-2zeL6SNnUsDVv9vG6A.png](1KoD-2zeL6SNnUsDVv9vG6A.png)

## Reading the file

Now we can read the optimized feather format file without any memory error. We can do pandas operations, functions, data analysis, data manipulation, and more.

![How%20did%20I%20convert%20the%2033%20GB%20Dataset%20into%20a%203%20GB%20fi%20f41babb6be074cb98b3e68e919f7e4c8/1nEtNBXB_pPROxbnofIhSSg.png](1nEtNBXB_pPROxbnofIhSSg.png)

We can do further optimization by analyzing ‘object ’ columns and converting them to ‘category’ or ‘string. We can do the same thing in other tools like dask and data table, but our aim is to deep dive into all the possibilities in the known territory and thus see pandas as a powerful tool. I hope this article will help handle the large datasets!

In case any queries or more clarification is needed, ping me on LinkedIn.

For more data science insights, connect with me on LinkedIn.

[https://www.linkedin.com/in/arunkumar-data-scientist/](https://www.linkedin.com/in/arunkumar-data-scientist/)

## [memory_optimiztion_amex_dataset](https://www.kaggle.com/code/arunkumardsci/memory-optimiztion-amex-dataset)

### [Explore and run machine learning code with Kaggle Notebooks | Using data from American Express - Default Prediction](https://www.kaggle.com/code/arunkumardsci/memory-optimiztion-amex-dataset)

[www.kaggle.com](https://www.kaggle.com/code/arunkumardsci/memory-optimiztion-amex-dataset)

Also, please check out my [GitHub repo,](https://github.com/kumarnarun/Amex-Default-Prediciton) if you want to download the complete working code.

See you in my next data science article, babye!