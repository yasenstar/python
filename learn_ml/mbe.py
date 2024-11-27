# 回归模型的评估指标
# pip install scikit-learn

from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, precision_score, recall_score, f1_score, classification_report, roc_auc_score, confusion_matrix
from sklearn import metrics
import numpy as np

y_true = [[0.5,1],[-1,1],[7,-6]]
y_pred = [[0,2],[-1,2],[8,-5]]
print(mean_absolute_error(y_true, y_pred))
print(mean_squared_error(y_true, y_pred))

# 分类模型的评估指标

x_true = [1,0,2,0,1,0,2,0,0,2]
x_pred = [1,0,1,0,0,0,2,0,2,1]
print(accuracy_score(x_true, x_pred, normalize=True))
print(accuracy_score(x_true, x_pred, normalize=False))
print(precision_score(x_true, x_pred, average=None))
print(precision_score(x_true, x_pred, average='micro'))
print(precision_score(x_true, x_pred, average='weighted'))
print(precision_score(x_true, x_pred, average='macro'))
print(recall_score(x_true, x_pred, average='weighted'))
print(f1_score(x_true, x_pred, pos_label=1, average='weighted'))

target_names = ['class 0', 'class 1', 'class 2']
print(classification_report(x_true, x_pred, target_names=target_names))

print(metrics.roc_curve(x_true, x_pred, pos_label=1))

print(confusion_matrix(x_true, x_pred, labels=[0,1,2]))

z_true = np.array([0,0,1,1])
z_pred_prob = np.array([0.1, 0.4, 0.35, 0.8])

print(roc_auc_score(z_true, z_pred_prob))