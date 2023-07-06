# seleniumforest



## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithm description](#algorithm-description)
* [License Agreement](#license-agreement)

## General info
This project contains the code for my master thesis. 
	
## Technologies
Project is created with:
* Python 3.7.9

  Other Python versions led to dependecy errors during the modul install. Therefore, I recommend to use 3.7.9.

	
## Setup
To run this project, install the following modules locally by using pip or your package manager of choice:

```
%pip install shap
%pip install numpy
%pip install pandas
%pip install pyspark
%pip install matplotlib
%pip install azure.identity
%pip install azure.digitaltwins.core
```

## Algorithm Description

```
Generate Model
```
The code generates a JSON file to set up the first Digital Twin instance on the Microsoft Azure platform. As input use the 'robotic-arms.csv'. The original CSV contains columns that are not used during this project. Therefore, it is recommended to delete the unwanted ones before generating the model.


## License agreement
The applied license can be found here:
[MIT License](https://github.com/h1548782/seleniumforest/blob/main/MIT-LICENSE.txt)
