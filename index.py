# Install if not already done
# pip install aif360 pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing

# Load dataset
dataset = CompasDataset()

# Check for disparate impact
metric = BinaryLabelDatasetMetric(dataset, privileged_groups=[{'race': 1}], unprivileged_groups=[{'race': 0}])
print("Disparate Impact:", metric.disparate_impact())

# Visualization: Distribution by Race
dataset.convert_to_dataframe()[0]['race'].value_counts().plot(kind='bar')
plt.title("Distribution by Race in COMPAS Dataset")
plt.xlabel("Race")
plt.ylabel("Count")
plt.show()
