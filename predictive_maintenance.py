import matplotlib
matplotlib.use('TkAgg')
import shap

def explain_prediction(df, index, model):
    #this only works for local predictions (single instances)
    #find first anomaly in test set

    shap.initjs()

    #Create Explainer
    explainer = shap.Explainer(model)  
    #Shap value for specific instance
    shap_values = explainer.shap_values(df.iloc[index]) 

    #force plot for that specific instance 
    force_plot = shap.force_plot(explainer.expected_value[0], shap_values[0], df.iloc[index])
    
    return force_plot