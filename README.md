# Predictive Maintenance in the Robotic Arms Industry by applying Digital Twin Technology



## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithm description](#algorithm-description)
	* [Python Scripts](#python-scripts)
   	* [Simulation](#simulation)
* [License agreement](#license-agreement)

## General info
This project contains the code for my master thesis. The video below offers a quick overview about the proposed framework.



https://github.com/h1548782/seleniumforest/assets/137823205/8cd7ae02-ea2a-4209-8dcb-6ee301cc4f49




https://github.com/h1548782/seleniumforest/assets/137823205/20f58627-d19d-4a0f-affb-84929a0e356c



	
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
This script focuses on the predictive maintenance. By using SHAP and it´s benefits in explainability for machine learning algorithms, the causes for the anomalies can be pin-pointed and countermeasures initiated. Here is an exmaple for the generated SHAP beeswarm plot for the SHAP values of all predicted anomalies. Dots marked in red, display high feature value, whereas features marked in blue, display low feature value. 
![shap_beeswarm_simulation](https://github.com/h1548782/seleniumforest/assets/137823205/fb5dd377-db2d-4553-b2e0-763122cf2bbd)

Furthermore, it contains code for a SHAP partial dependence plot. That way, specific features can be analyzed in more detail, giving more insight into the prediction process.
![shap_partial_dependence_plot](https://github.com/h1548782/seleniumforest/assets/137823205/6f512bcf-5dce-4406-898c-23d33a30bc3d)





### Simulation
#### _simulation_robotic_arm.ipynb_
The scripts mentioned above are used to run the simulation of a running robotic arm. The main notebook for this purpose is the simulation_robotic_arm.ipynb jupyter file. It imports the predefined functions from all of the available python scripts. A detailed description of each function can be found within the script files.




## License agreement
The applied license can be found here:
[MIT License](https://github.com/h1548782/seleniumforest/blob/main/MIT-LICENSE.txt)
