# seleniumforest



## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithm description](#algorithm-description)
* [License agreement](#license-agreement)

## General info
This project contains the code for my master thesis. 
	
## Technologies
Project is created with:
* Python 3.7.9

  Other Python versions led to dependecy errors during the modul install. Therefore, I recommend to use 3.7.9.

* Microsoft Azure - Digital Twin Platform

* Microsoft Visual Studio Code IDE

	
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

In addition to an active Mincrosoft Azure account, the Microsoft Azure CLI is also neccessary. It can be downloaded here:

[Azure CLI](https://ojuliuscoder.medium.com/installing-and-using-azure-cli-in-visual-studio-code-a382d2b09bfa)

## Algorithm Description

```
Generate Model
```
The code generates a JSON file to set up the first Digital Twin instance on the Microsoft Azure platform. As input use the 'robotic-arms.csv'. The original CSV contains columns that are not used during this project. Therefore, it is recommended to delete the unwanted ones before generating the model.

```
!az login
```
A browser window will open and you will be asked to enter your Azure credentials. This enables the usage of Azure functionalities within VSC, without having to manually authenticate. 

```
Random Forest
```
Builds a random forest model with the provided training data. At the end, the accuracy score and confusion matrix of the test set will be printed.

```
Permutation Importance
```
Displays the permutation feature importance of the training data. At the end it prints the regarding importance score for each feature used. Additionaly, the standard deviation for each feature is displayed.


## License agreement
The applied license can be found here:
[MIT License](https://github.com/h1548782/seleniumforest/blob/main/MIT-LICENSE.txt)
