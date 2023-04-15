import os

dirs = [
    "saved_models",
    "logs",
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    os.path.join("src","components"),
    os.path.join("webapp","static","css"),
    os.path.join("webapp","templates")
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "README.md",
    "requirements.txt",
    ".gitigonre",
    "dvc.yaml",
    "params.yaml",
    os.path.join("src/components","__init__.py"),
    os.path.join("src/components","sox_model_train_dag.py"),
    os.path.join("src/components","sox_prediction_dag.py"),
    os.path.join("webapp/templates","index.html"),
    os.path.join("webapp/templates","404.html"),
    os.path.join("webapp/static/css","style.css"),
    "app.py"
]

for file_ in files:
    with open(file_, "w") as f:
        pass

# files = [
#     "dvc.yaml",
#     "params.yaml",
#     ".gitignore",
#     os.path.join("src","__init__.py")
# ]

# for file_ in files:
#     with open(file_, "w") as f:
#         pass