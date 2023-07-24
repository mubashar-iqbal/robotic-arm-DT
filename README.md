# seleniumforest



## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithm description](#algorithm-description)
	* [Python Scripts](#python-scripts)
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

In addition to an active Microsoft Azure account, the Microsoft Azure CLI is also neccessary. It can be downloaded here:

[Azure CLI](https://ojuliuscoder.medium.com/installing-and-using-azure-cli-in-visual-studio-code-a382d2b09bfa)

Make sure that the correct Digital Twin schema is setup on the Azure platform. Otherwise parts of the code will not run properly. To set it up, use _digital-twin-schema.json_ in the upload model section. It already contains the five neccassary sensor components to simulate a robotic arm.

## Algorithm Description

### Python Scripts

#### _digital_twin_azure.py_
This script contains all steps related to the Digital Twin instance on the Microsoft Azure platform. It contains a function to connect to via browser, gathering available twin information, and lastly a function to send data to the Digital Twin. The script also includes the code for plotting a dashboard-like monitoring system. The system will display the current workload of the robotic arm´s components and the current anomaly state. Furthremore, it includes a visual alarm to display anomaly occurrences.
![dashboard](https://github.com/h1548782/seleniumforest/assets/137823205/26feb273-7a63-4879-b92a-2bc5eca3c673)

#### _anomaly_detection.py_
This file contains all code neccessary to train a prediction model and furthermore predict loval instances. The function train_model() will create a random forest model, based on the provided input. Additionally, it will display the achived accuracy score and show a confusion matrix. predict_model() can then be used to predict the anomaly state for current instances. 

#### _predictive_maintenance.py_
This script focuses on the predictive maintenance. By using SHAP and it´s benefits in explainability for machine learning algorithms, the causes for the anomalies can be pin-pointed and countermease initiated. Here is an exmaple for the generated SHAP bar plot in case of a detected anomaly. Each bar represents an individual components/feature. Features marked in red, positivly contributed to the prediction. Be aware, that it only indicates correlation to the output of the prediction and not to a specific instance of the output. 
![shap-bar-plot](https://github.com/h1548782/seleniumforest/assets/137823205/141bce59-5e14-4d18-a441-7f583fe05dc2)



### Simulation
#### _Selenium Forest.ipynb_
The following functions are used to run the simulation of a running robotic arm. The main notebook used for this is the Selenium Forest.ipynb jupyter file. It imports the predefined function from all of the available python scripts (see above). A detailed description of each function can be found within the scripts.




## License agreement
The applied license can be found here:
[MIT License](https://github.com/h1548782/seleniumforest/blob/main/MIT-LICENSE.txt)
