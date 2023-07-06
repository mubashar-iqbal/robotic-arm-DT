# seleniumforest



## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithm description](#algorithm-description)
	* [Pre-requisites](#pre-requisites)
   	* [Simulation](#simulation)
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

### Pre-requisites

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

```
SHAP
```
The SHAP section focuses on providing further insight into the various features. It shows plot of either global or local instances. Furthermore, there is a seperation between normal and anamolous occurences. 

### Simulation
The following functions are used to run the simulation of a running robotic arm. During the simulation, the test set of the previously build train- and test split was used. It is neccessary to run each code cell before starting the simulation, as it requires trained models to run without errors.

```
select_row()
```
This function fetches a specific line out of the provided dataframe by using the name of the dataframe and the desired index row as input. This data will then be used to update the model on the Azure platform.

```
update_machine()
```
This cell applies the previously generated function _select_row()_ and updates the existing model on the Azure platform. In addition, to the inputs required for _select_row()_ the function also requires the Digital Twin´s name in order to indentify the correct twin instance.

```
predict_model()
```
This function requires the dataframe used for simulation, the index identifying a specific row, and a trained model as input. It transforms the row of data into processable form and predicts if the occurence is an anomaly or not, given the earlier trained random forest model. 

```
start_machine()
```
By starting the machine, the code will iterate over the available simulation dataframe. For each entry the function will update the model on Azure platform with _update_machine()_ and furthermore, predict if the current data suggests the occurence of anomalies. This will be done every second, however speed can be adjusted with the _time.sleep()_ module, depending on  local available computing power. 


## License agreement
The applied license can be found here:
[MIT License](https://github.com/h1548782/seleniumforest/blob/main/MIT-LICENSE.txt)
