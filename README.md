# Versioning-ML-Models-datasets-With-DVC

Data Version Control, or DVC, is a data and ML experiment management tool that takes advantage of the existing engineering toolset that we are familiar with (Git, CI/CD, etc.). DVC is meant to be run alongside Git. The git and DVC commands will often be used in tandem, one after the other. While Git is used to storing and version code, DVC does the same for data and model files.


# DVC

**If you don’t have DVC Install then install as below.**
```
pip install dvc
```

**Getting started with DVC:**

```
dvc init
```

**We need to tell DVC where our remote storage is on local machine:**

```
dvc add  /data_given/SAHeart.csv
```

**DVC pipeline:**

```
dvc dag
```

```
dvc repro
```
**Model Metrics:**

```
dvc metrics show
```

**Model Plots:**
```
dvc plots show result/cm.csv --template confusion -x chd -y Predicted
```

```
dvc metrics diff
```

```
dvc plots show result/cm.csv --template confusion -x chd -y Predicted
```