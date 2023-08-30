import matplotlib
matplotlib.use('TkAgg')
import shap
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def explain_prediction(X_train, y_train, X_test, sample_ind):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_predicted = model.predict(X_test)

        explainer = shap.Explainer(model)
        shap_values = explainer(X_test)

        positive_indices = np.where(y_predicted == 1)[0]
        shap_values_positive = shap_values[positive_indices, :, 1]

        beeswarm = shap.plots.beeswarm(shap_values_positive)
        
        #Generate partial dependence plot
        #This code generates a SHAP partial dependence plot for a specific instance.
        #The instance can be chosen by chaning the sample_ind value (integer).
        sample_ind = sample_ind
        pdp = shap.partial_dependence_plot(
        "Tool_Temperature", model.predict, X_test, model_expected_value=True,
        feature_expected_value=True, ice=False,
        shap_values=shap_values_positive[sample_ind:sample_ind+1,:]
        )
        
        return beeswarm, pdp

