import matplotlib
matplotlib.use('TkAgg')
import shap

#this function will be used in case an anomaly was detected with predict_model() from anomaly_detection.py.
#it displays a shap plot to showcase which sensor component was responsible for the prediction of the anomaly.
def explain_prediction(df, index, model):
    #this only works for local predictions (single instances)
    #find first anomaly in test set

    shap.initjs()

    #Create Explainer
    #explainer = shap.Explainer(model)
    #Shap value for specific instance
    #shap_values = explainer.shap_values(df.iloc[index]) 

    #force plot for that specific instance 
    #force_plot = shap.force_plot(explainer.expected_value[0], shap_values[0], df.iloc[index])
    #bar_plot = shap.plots.bar(shap_values[0])
    
    
        # Create Explainer
    explainer = shap.Explainer(model)
    # SHAP values for specific instance
    shap_values = explainer.shap_values(df.iloc[index])

    # Create a SHAP Explanation object for the specific instance
    explanation = shap.Explanation(values=shap_values[0], base_values=explainer.expected_value[0], data=df.iloc[index])

    # Bar plot for feature importances of the specific instance
    bar_plot = shap.plots.bar(explanation)
    
    return bar_plot
    