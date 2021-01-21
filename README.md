[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![NSF-1928366](https://img.shields.io/badge/NSF-1928366-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1928366)

# Neotoma Recommender

Project to create a pipeline that uses Graph Recommendation Systems to recommend whether Throughput Article is of interest to the Neotoma Database.

Using Graph Databases and a Data Science approach, identify whether a paper is suitable for Neotoma and detect interesting features such as 'number of commits', 'last updates', 'number of linked repos' and 'linked databases'.  

Baseline Model will be a Recommender System in unstructured Graph Databases and data will also tried to be structured to create a Recommendre System using Python.

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
│   ├── input                       # input data
│   │     ├── throughput neo4j db   # data: paleoecology db - dummy file for reproducibility
│   │     └── neotoma_db            # data: bibliography json dummy file for reproducibility
│   ├── output                      # output file
│   │     └── predictions.csv   # file to describe whether an article belongs to neotoma or not
├── img                        # all images or docs for explaining processes
├── reports    
│   ├── milestones
│   └── supporting documents           
├── src    
│   ├── preprocessing    
│   │     └── data_preprocessing.py    # script to clean data
│   ├── train                          # scripts for helping functions and training model
│   │     ├── utils.py
│   │     └── train.py                 
│   └──  predict                 # prediction scripts to validate test data and to try in new data
│   │     └── predict.py       
├── .gitignore
├── config_sample.py             # file for credentials
├── CODE_OF_CONDUCT.md
├── LICENSE
└── README.md
```

### Workflow Overview

This project uses the Throughput Graph Database as an input from neo4j:
* `neotoma:` tsv file

These files are used as input that will help create a Recommender System.
* Predict whether an article is suitable for Neotoma.
* Create nodes in Throughput graph / Create a Graph for Neotoma Files
* Benefit from operations using Graph Databases.

### System Requirements

This project is developed using Python and Neo4j.  
This project will need Neo4j installed.
It runs on a MacOS system.
Continuous integration uses TravisCI.

### Data Requirements

The project pulls data from the Throughput database.

### Key Outputs

This project will generate a structured dataset that provides the following information:
* Whether the paper is useful for Neotoma based on its characteristics or not.

## Pipeline
TODO:
\n
\n

[include workflow chart]

### Instructions

For now, only the notebook is available.
There will be scripts shortly.
