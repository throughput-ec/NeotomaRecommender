[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![NSF-1928366](https://img.shields.io/badge/NSF-1928366-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1928366)

# Neotoma Recommender

Project to create a pipeline that uses Recommendation Systems to recommend a Throughput Article to the Neotoma Database.

Using NLP parsed text and a Data Science approach, identify whether a paper is suitable for Neotoma and detect features such as 'Site Name', 'Location', 'Age Span' and 'Site Descriptions'.  

Baseline Model is Naive Bayes to classify if a Throughput article belongs or not to Neotoma.

## Contributors

This project is an open project, and contributions are welcome from any individual.  All contributors to this project are bound by a [code of conduct](CODE_OF_CONDUCT.md).  Please review and follow this code of conduct as part of your contribution.

  * [Simon Goring](http://www.goring.org/) [![orcid](https://img.shields.io/badge/orcid-0000--0002--2700--4605-brightgreen.svg)](https://orcid.org/0000-0002-2700-4605)
  * [Socorro Dominguez Vidana](https://sedv8808.github.io/) [![orcid](https://img.shields.io/badge/orcid-0000--0002--7926--4935-brightgreen.svg)](https://orcid.org/0000-0002-7926-4935)


### Tips for Contributing

Issues and bug reports are always welcome.  Code clean-up, and feature additions can be done either through branches.

All products of the Throughput Annotation Project are licensed under an [MIT License](LICENSE) unless otherwise noted.

## How to use this repository

Files and directory structure in the repository are as follows:
This structure might be modified as the project progresses.

```bash
throughput-ec/neotoma_recommender/
├── data
│   ├── input                 # input data
│   │     ├── neotoma_dummy   # data: paleoecology db - dummy file for reproducibility
│   │     └── bibjson_dummy   # data: bibliography json dummy file for reproducibility
│   ├── output                # output file
│   │     └── predictions.csv   # file to describe whether an article belongs to neotoma or not
├── figures                   # all images or docs for explaining processes
│   ├── img
│   └── docs
│   │     └── milestones                    
├── src    
│   ├── modules               # 3 modules
│   │   ├── preprocessing    
│   │   │     └── data_preprocessing.py    # script to clean data
│   │   ├── train                          # scripts for helping functions and training model
│   │   │     ├── utils.py
│   │   │     └── fit.py                 
│   │   └──  predict                 # prediction scripts to validate test data and to try in new data
│   │   │     └── predict.py       
│   ├── tests                        # tests for the modules
│   │   ├── test_preprocessing                                       
│   │   ├── test_fit.py                      
│   └── └── test_predict.py
├── .gitignore
├── CODE_OF_CONDUCT.md
├── Dockerfile
├── LICENSE
└── README.md
```

### Workflow Overview

This project uses the GeoDeepDive output files:
* `bibjson:` JSON file that contains bibliographic information.
* `neotoma:` tsv file that contains Netoma paleoecology database information.

These files are used as input in a Naive Bayes baseline model that, once trained, should:
* Predict whether a sentence has coordinates or not in it.


TODO
* We will then produce a recommendations system using Python to see if an article should be part of the Neotoma Database or not.

* Create nodes in Throughput graph / Create a Graph for Neotoma Files
* Create a recommendation system using Neo4j using Graph characteristics.


### System Requirements

This project is developed using Python.  
This project will need Neo4j installed.
It runs on a MacOS system.
Continuous integration uses TravisCI.

### Data Requirements

The project pulls data from GeoDeepDive output files.
For the sake of reproducibility, two dummy data files have been included.

### Key Outputs

This project will generate a dataset that provides the following information:
* Whether the paper is useful for Neotoma based on the title.

## Pipeline
TODO:
\n
\n

[include workflow chart]

### Instructions

There are currently two main functionalities for this repo.
The first one is to run a Dashboard that will help us hand label new data in order to improve Record Mining predictions.

If you are helping to hand label, these are the instructions you should follow:

##### Docker neotoma_recommender
TODO : verify and upload image

If you are trying to get new predictions on never seen corpus, then follow these instructions:

1. Clone/download this repository.
2. Using the command line, go to the root directory of this repository.
3. Get the [neotoma_recommender]() image from [DockerHub](https://hub.docker.com/) from the command line:
```
docker pull sedv8808/neotoma_recommender
```
4. Verify you are in the root directory of this project. Type the following (filling in *\<Path_on_your_computer\>* with the absolute path to the root of this project on your computer).

```
docker run -v /<Path_on_your_computer>/neotoma_recommender/data/input:/app/input
 -v /<Path_on_your_computer>/neotoma_recommender/data/output:/app/output neotoma_recommender:latest
```
5. You will get an output file with a timestamp. That file are your predictions. You can verify whether those outputs belong to Neotoma using a `Confusion Matrix`

**IMPORTANT:** In order to run this docker file, you need to load in the `data` directory a `bibjson` file and a `neotoma` that respect the same format as the dummy files.

##### Without Docker and to review other scripts.

This repository consists of 4 Python scripts.

In order to run this project, you need to:
1. Clone or download this repository.

2. Run the following code in the terminal at the project's root repository.
To run the scripts:

```
# From the command line.

# Load and preprocess data
python3 src/modules/preprocessing/preprocess_data.py

# Train model - Optional/Only when retraining is needed
python3 src/modules/train/train.py

# Predict on new data
python3 src/modules/modelling/predict.py
```


##  Profiling
Detailed profiling logs can be found on:
```
output/profiling
```

If you want to repeat a detailed profiling for each script, open `preprocess_data.py`, `fit.py` and `predict.py`.
The scripts, at the bottom, have a commented chunk of code titled `Profiling`.
This profiling is recommended to only be run once. Once you finished this, comment the chunk again.

#### preprocess_data.py


#### fit.py

#### predict.py
