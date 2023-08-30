import matplotlib.pyplot as plt
from IPython.display import clear_output, display
from ipywidgets import Output, VBox, Button
from matplotlib import image as mpimg

from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
from azure.identity import VisualStudioCodeCredential
import os

#this function can be used to connect to the microsoft azure platform.
#insert the url of the specific azure instance you want to connect to.
#afterwards the service_client will be returned, which can further be used to push updates to the twin
def connect_azure():
    #getting the credentials

    #define the URL of Digital Twin instance on the Azure platform
    url = "SeleniumForest.api.weu.digitaltwins.azure.net"

    #store the gathered credentials in a variable
    credential = DefaultAzureCredential()
    #create an instance of the Digital Twin Client
    #it can be resued later on
    global service_client
    service_client = DigitalTwinsClient(url, credential)
    
    return service_client

#this function fetches the data of a dataset for a given index. It will
#later be be used to get the feature data during the simulation
def select_row(df, index):
    row = df.loc[index]

    for col_name, value in row.items():
        locals()[col_name] = value

    #Return variables
    return locals()

#this function enables to get the stored values on the digital twin model.
#the twin_id represents the name given to the twin (in this case 'RoboArm')
#furthremore, the service_client must be provided
#lastly, the component defines which component data should be accessed (which sensor)
def get_twin_state(twin_id, service_client, component):
    twin = service_client.get_digital_twin(twin_id)
    twin_state_value = twin[component]
    return twin_state_value

#this function updated the digital twin on the microsoft azure platform.
#to do so, it takes the newly received data from the simulation dataset by applying the select_row() function
#also, it stores the value that was predicted for the current anomaly state.
#all of these values are then sent to the digital twin
#to check if the data was sent correctly, I would recommend to check the values on the digital twin UI itself.
def update_machine(model_name: str, df, index, y_predicted):
    new_data = select_row(df, index)
    pred_anomaly = y_predicted

    patchModel = [
      {
    "op": "replace",
    "path": "/Norm_of_Cartesion_Linear_Momentum",
    "value": float(new_data['Norm_of_Cartesion_Linear_Momentum'])
  },
      {
    "op": "replace",
    "path": "/Robot_Current",
    "value": float(new_data['Robot_Current'])
  },
      {
    "op": "replace",
    "path": "/Tool_Current",
    "value": float(new_data['Tool_Current'])
  },
      {
    "op": "replace",
    "path": "/Tool_Temperature",
    "value": float(new_data['Tool_Temperature'])
  },
      {
    "op": "replace",
    "path": "/TCP_Force",
    "value": float(new_data['TCP_Force'])
  },
      
      {
    "op": "replace",
    "path": "/Anomaly_State",
    "value": int(pred_anomaly)
  }
]
    service_client.update_digital_twin(model_name, patchModel)

#requires additional code to be updated automatically
#this function plots the values currently stored in the digital twin
#furthermore, it acts as something similar to a dashboard.
#all of the current values are displayed in barplots.
#in case an anomaly was found during predict_model(), the plot will display an alert message
def plot_twin_state(_=None):
    norm_of_cartesion_linear_momentum = get_twin_state('RoboArm', service_client, 'Norm_of_Cartesion_Linear_Momentum')
    robot_current = get_twin_state('RoboArm', service_client, 'Robot_Current')
    tool_current = get_twin_state('RoboArm', service_client, 'Tool_Current')
    tool_temperature = get_twin_state('RoboArm', service_client, 'Tool_Temperature')
    tcp_force = get_twin_state('RoboArm', service_client, 'TCP_Force')
    anomaly_state = get_twin_state('RoboArm', service_client, 'Anomaly_State')
    
    # Create subplots
    plt.rcParams["figure.figsize"] = (12, 7)
    figure, axis = plt.subplots(1, 6)
    plt.subplots_adjust(wspace=1)
    plt.suptitle("Digital Twin´s State")
    
    # Norm_of_Cartesion_Linear_Momentum
    axis[0].bar(x=0, height=norm_of_cartesion_linear_momentum, width=1, align='center', alpha=1, color="#22a7f0")
    axis[0].set_xticks([])
    axis[0].set_xlabel('Linear Momentum')
    axis[0].set_ylabel('')
    axis[0].set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
    
    # Robot_Current
    axis[1].bar(x=0, height=robot_current, width=1, align='center', alpha=1, color="#e14b31")
    axis[1].set_xticks([])
    axis[1].set_xlabel('Robot Current')
    axis[1].set_ylabel('A')
    axis[1].set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
    
    # Tool_Current
    axis[2].bar(x=0, height=tool_current, width=1, align='center', alpha=1, color="#76c68f")
    axis[2].set_xticks([])
    axis[2].set_xlabel('Tool Current')
    axis[2].set_ylabel('A')
    axis[2].set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    
    # Tool_Temperature
    axis[3].bar(x=0, height=tool_temperature, width=1, align='center', alpha=1, color="#f5ec42")
    axis[3].set_xticks([])
    axis[3].set_xlabel('Tool Temperature')
    axis[3].set_ylabel('Celcius')
    axis[3].set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    
    # TCP_Force
    axis[4].bar(x=0, height=tcp_force, width=1, align='center', alpha=1, color="#804aba")
    axis[4].set_xticks([])
    axis[4].set_xlabel('TCP Force')
    axis[4].set_ylabel('N')
    axis[4].set_yticks([1, 3, 5, 7, 9, 11, 13, 15, 17])
    
    # Anomaly_State
    alarm_color = "#ff0000" if anomaly_state else "#00ff00"
    alarm_text = "Attention: Anomaly Detected" if anomaly_state else "Normal"
    axis[5].text(0.5, 0.5, alarm_text, ha='center', va='center', fontsize=18, color=alarm_color)
    axis[5].axis('off')
    
    if anomaly_state:
        # Alarm Image
        alarm_img_path = "./Data/alarm.jpg"
        alarm_img = mpimg.imread(alarm_img_path)
        axis[5].imshow(alarm_img)
    
    # Show all plots
    plt.show()
    clear_output(wait=True)

