# Summary of 4_Default_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.075
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **eval_metric**: mlogloss
- **num_class**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

2.0 seconds

### Metric details
|           |   0 |        1 |         2 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   1 | 1        |  0.909091 |   0.962963 |    0.969697 |       0.96633  |  0.201688 |
| recall    |   1 | 0.888889 |  1        |   0.962963 |    0.962963 |       0.962963 |  0.201688 |
| f1-score  |   1 | 0.941176 |  0.952381 |   0.962963 |    0.964519 |       0.962755 |  0.201688 |
| support   |   8 | 9        | 10        |   0.962963 |   27        |      27        |  0.201688 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |
|:-------------|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                8 |                0 |                0 |
| Labeled as 1 |                0 |                8 |                1 |
| Labeled as 2 |                0 |                0 |               10 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
