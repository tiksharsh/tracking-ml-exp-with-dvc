import os

dirs = [
    "saved_models",
    "logs",
    "report",
    "data_given",
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    os.path.join("src","components"),
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    # with open(os.path.join(dir_, ".gitkeep"), "w") as f:
    #     pass

files = [
    "README.md",
    "requirements.txt",
    ".gitigonre",
    "dvc.yaml",
    "params.yaml",
    os.path.join("src/components","__init__.py"),
    os.path.join("src/components","get_data.py"),
    os.path.join("src/components","load_data.py"),
    os.path.join("src/components","split_data.py"),
    os.path.join("src/components","train_and_evaluate.py"),
    "app.py"
]

for file_ in files:
    with open(file_, "w") as f:
        pass
