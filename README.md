# Exploring How Corona Relate to Happiness Factors Worldwide

![grafik](https://github.com/EnigmaticAbyss/Methods-of-data-engineering-ss2024/assets/69069319/06a31011-badc-4fc1-9193-7825ec268729)

This project looks at how various types of crops had affected the climate change. We want to find if there is a link about increase of countries temprature and amount of crop that is being harvested. Here different messures of crop production such as seeds, yields and gross pro- duction are considred as well. My intention is to use statistics and some machine learning methods to find out a relation between crops and global warming so that we get better understanding of themost dangerous crops for environment as well.

## Porject report:
In this link you can find a final report for the given project with results:

https://github.com/EnigmaticAbyss/Methods-of-data-engineering-ss2024/blob/main/project/final-report.ipynb

## Data Exploration
if you are interested in exploring choosen dataset you can go over this file and see some visualization on them :

https://github.com/EnigmaticAbyss/Methods-of-data-engineering-ss2024/blob/main/project/data-exploration.ipynb
## Complete data analysis
if you are interested in understanding all the methods in the project and far more extensive look this link can be helpful. Here there are alternative methods and paths that were taken for the project :

https://github.com/EnigmaticAbyss/Methods-of-data-engineering-ss2024/blob/main/project/data_report.ipynb

## Presentation
in the following link you can also see the slides presenting this project as well:

https://github.com/EnigmaticAbyss/Methods-of-data-engineering-ss2024/main/project/slides.pdf

## Kaggle Authentication
In this project one of the datasets in provided by kaggle. For downloading and use it in this project, we need to use their authentication system which includes a kaggle.json file. 
you can get it from [link](https://www.kaggle.com/settings)
for more instruction and help about using kaggle api you can visit : 
after getting it, the file should be placed in `/project/kaggle.json`

**Filepath:** `/project/kaggle.json`

```
{"username":"e************s",
"key":"b**************************e"}
```


## how to use 

1. Clone this git repository.
```bash
git clone https://github.com/EnigmaticAbyss/Methods-of-data-engineering-ss2024.git
```

## First step : Run requirements installation

pip install -r ./project/requirements.txt

## second step : Run pipeline
```
./project/pipeline.sh
```

this pipeline is designed to run pipeline.py to read data from its source and do some cleaning and save the results in sqlite files in /data folder. Consider there are two types of data analysis afterwards which one is more extensive and the other one is a summerized version.
