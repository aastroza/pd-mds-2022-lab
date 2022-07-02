# Laboratorio - Implementando un modelo de Machine Learning

**Este Laboratorio está inspirado en la unidad 1 del curso [Introduction to Machine Learning in Production (DeepLearning.AI)](https://www.coursera.org/learn/introduction-to-machine-learning-in-production/home/welcome). También se apoya en código para generar el modelo disponible en [este repositorio de Shreya Shankar](https://github.com/shreyashankar/debugging-ml-talk) e implementar un flujo de trabajo usando Github Actions de la [Unidad 4 del curso mencionado anteriormente](https://github.com/jesussantana/DeepLearning.AI-Introduction-to-Machine-Learning-in-Production).**

Para comenzar deben haber bajado todos los archivos a una carpeta y en el terminal de Anaconda llegar a ese directorio.

```
.
└── pd-mds-2022-lab (este directorio)
    ├── model (acá irán nuestros modelos)
    ├── 00_nyc-taxi-model.ipynb
    ├── 01_server.ipynb
    ├── 02_client.ipynb
    └── requirements.txt (dependencias de Python)
```
 
 
## Pasos previos usando Conda
 
### Prerequisito: Tener [conda](https://docs.conda.io/en/latest/) instalado en tu computador.
 
Vamos a usar Conda para construir un entorno virtual nuevo.
 
### 1. Creando el entorno virtual (Virtual Environment)
 
Asumiremos que tenemos instalado conda. El primer paso es crear un nuevo enviroment para desarrollar. Para crear uno usando Python 3.8 debemos ejecutar el siguiente comando:
 
```bash
conda create --name pd-mds-2022-lab python=3.8
```
 
Luego debemos activarlo usando el comando:
 
```bash
conda activate pd-mds-2022-lab
```
 
Todo el trabajo que realicemos con este código será en este entorno. Así que al trabajarcon estos archivos siempre tiene que estar activo el ambiente pd-mds-2022-lab.
 
### 2. Instalando las dependencias usando PIP 
 
Antes de seguir, verifica que en el terminal de Anaconda estés dentro del directorio `pd-mds-2022-lab`, el cual incluye el archivo `requirements.txt`. Este archivo enlista todas las dependencias necesarias y podemos usarlo para instalarlas todas:
 
```bash
pip install -r requirements.txt
```
 
Este comando puede demorar un rato dependiendo de la velocidad del computador y la de la conexión a Internet. Una vez que termine ya está listo todo para comenzar una sesión de Jupyter Lab o Notebook.

Luego debemos enlazar el kernel de jupyter lab a nuestro nuevo enviroment:

```bash
python -m ipykernel install --user --name pd-mds-2022-lab
```

 
### 3. Iniciando Jupyter Lab
 
Jupyter lab debería haber quedado instalado en el paso anterior, así que basta con escribir:

```bash
jupyter lab
```

### 4. Generando modelo de ML

El notebook que genera el modelo se puede ejecutar en su totalidad desde [Google Colab](https://drive.google.com/file/d/19R8yRdgGOIuGCBmHZQibADRbz_JRV6tt/view?usp=sharing).


## Agregando pipelines de CI/CD usando GitHub Actions

En este laboratorio también usaremos [GitHub Actions](https://github.com/features/actions) para automatizar flujos de trabajo de Machine Learning. Además haremos un test unitario simple usando [pytest](https://docs.pytest.org/en/6.2.x/) para evaluar cambios en el código antes de publicar a producción.

Para esta parte debemos hacer un [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) de este repositorio para que podamos correr las GH actions en nuestra propia copia del repositorio.



### ¿Qué es GH Actions?

This is an amazing tool that allows you to define automatic workflows for specific events within a GH repo. For instance you can create Python script versions of all your Jupyter notebooks every time you push or pull changes from the remote repository.

In this lab you will set up an action that will run the unit tests defined for your code every time you push changes to the remote repo.

To give you an idea of the flexibility of this tool, you could also (although not covered in this lab) set the action to build a Docker image out of your code if all the unit tests were passed and sent that image to a Google Cloud Bucket where it can be used to deploy your code. This would mean that you successfully automated your deployment with every push of changes.


## Fork the public repo

Forking a repo is simply creating your own copy of it. It is often used in Open Source development as a way of keeping everything tidy. Instead of working directly on a public repo (in which you probably won't have writing access) you can work on your fork and submit Pull Requests from it. To fork a repo just click on the `Fork` button on the top right corner of the repo:

![fork-repo](assets/fork-repo.PNG)


Once the forking process has been completed you should have a copy of the repo registered under your username, like this:

![your-fork](assets/your-fork.PNG)

Now you need to clone it into your local machine. You can do so by using these commands (be sure to replace the username used here for your own):

```bash
git clone https://github.com/your-username/pd-mds-2022-lab.git
```


Now you need to enable Actions for your fork. You can do so by clicking on the Actions button:

![action-button](assets/action-button.PNG)

And clicking the green button to enable Actions:

![enable-actions](assets/enable-actions.PNG)

## Navigating the fork

Now `cd` into your fork. You can do so by using the command `cd machine-learning-engineering-for-production-public` while on the directory that contains your fork.

Before jumping to the directory with the files for this lab, notice a hidden folder in the root of the repo called `.github`. Within there is another directory called `workflows`, here is where all of the files for configuring Actions should be placed. These files should be in `YAML` format. In this case you should encounter a file called `course4-week3-lab.yml` that will be responsible for setting up your desired action of running unit tests. For convenience the contents of the file are placed here:

```yml
# Run unit tests for your Python application

name: PD-MDS-Lab

# Controls when the action will run. 
on:
  # Triggers the workflow on push request events only when there are changes in the desired path
  push:
    paths:
      - 'app/**'

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "test"
  test:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest
    defaults:
      run:
        # Use bash as the shell
        shell: bash


    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      -
        name: Checkout
        uses: actions/checkout@v2
      - 
        name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8.2'
      - 
        name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      -
        name: Test with pytest
        run: |
          cd app/
          pytest
```

Wow that is a long file. Let's break it down piece by piece (notice that comments are trimmed to keep the snippets short but they also provide important information so be sure to read them if you don't understand something):

```yml
name: PD-MDS-Lab
on:
  push:
    paths:
      - 'app/**'
```

In this first part you need to define a name for your Action so you can differentiate it from other ones. After this you need to specify what will trigger it, in this case the Action will be run automatically with a **push** that has changes to any file within the `course4/week3-ungraded-labs/C4_W3_Lab_4_Github_Actions` directory.

```yml
jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
```

In the next part you need to define all of the jobs than will run when this action is triggered. In this case you only need one job, which will be named `test` and will run in an environment that uses the latest release of Ubuntu. You can also define some default behavior for the job such as the desired shell, `bash` in this case, and the working directory within the repo. This means that the action will run as it had `cd` into the `course4/week3-ungraded-labs/C4_W3_Lab_4_Github_Actions/` directory first.

```yml
    steps:
      -
        name: Checkout
        uses: actions/checkout@v2
      - 
        name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8.2'
      - 
        name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      -
        name: Test with pytest
        run: |
          cd app/
          pytest
```

Finally you need to specify the `steps` for this action to be completed. This is a sequence of commands to achieve the functionality you strive for.  `steps` have several values associated such as:
- `name`: The name of the step.

- `uses`: You can specify an already existing `Action` as an step on one of your own. This is pretty cool because it allows for reutilization of Actions. 
- `run`: Instead of using an existing Action you might need to run a command. Since you are using `bash` inside a Linux VM, these commands should follow the correct syntax.
- `with`: You might need to specify some additional values. This field is for such cases.


Let's understand every step in order:

- The first step uses the `actions/checkout@v2` Action. This is usually included in every Action since it allows GitHub to access or check-out your repo.

- Now that your repo has been checked-out, you need to set an environment capable of running your Python code. To accomplish this the `actions/setup-python@v2` Actions is used while specifying the desired Python version.
- Having a Python supported environment it is time to install of the dependencies that your application needs. You can do so by using upgrading `pip` and then using it to install the dependencies listed in the `requirements.txt` file.
- Finally you can run your unit tests by simply using the `pytest` command. Notice that you needed to `cd` into the `app` directory first.

Now that you have a better sense of how to configure Actions it is time to put them to test.

## Testing the CI/CD pipeline

Within the `app` directory a copy of the server that serves predictions for the Wine dataset (that you used in a previous ungraded lab) is provided. The file is the same as in that previous lab with the exception that the classifier is loaded directly into global state instead of within a function that runs when the server is started. This is done because you will be performing unit tests on the classifier without starting the server.

### Unit testing with pytest

To perform unit testing you will use the `pytest` library. When using this library you should place your tests within a Python script that starts with the prefix `test_`, in this case it is called `test_clf.py` as you will be testing the classifier. 

Let's take a look at the contents of this file:

```python
import pandas as pd
from main import rfc
from sklearn.metrics import f1_score

def test_accuracy():

    # Load test data
    taxi_test = pd.read_csv('./data/yellow_tripdata_2020-03_test.csv')

    numeric_feat = [
    "pickup_weekday",
    "pickup_hour",
    'work_hours',
    "pickup_minute",
    "passenger_count",
    'trip_distance',
    'trip_time',
    'trip_speed'
    ]
    categorical_feat = [
        "PULocationID",
        "DOLocationID",
        "RatecodeID",
    ]

    features = numeric_feat + categorical_feat
    target_col = "high_tip"

    # Predict test examples
    preds_test = rfc.predict_proba(taxi_test[features])
    preds_test_labels = [p[1] for p in preds_test.round()]

    # Compute f1-score of classifier
    f1 = f1_score(taxi_test[target_col], preds_test_labels)


    # f1-score should be over 0.7
    assert f1 > 0.7
```

There is only one unit test defined in the `test_accuracy` function. This function loads the test data that was saved in pickle format and is located in the `data/test_data.pkl` file. Then it uses this data to compute the accuracy of the classifier on this test data. Something important is that this data is **not scaled** as the test expects the classifier to be a `sklearn.pipeline.Pipeline` which first step is a `sklearn.preprocessing.StandardScaler`.

If the accuracy is greater than 90% then the test passes. Otherwise it fails.

## Running the GitHub Action

To run the unit test using the CI/CD pipeline you need to push some changes to the remote repository. To do this, **add a comment somewhere in the `main.py` file and save the changes**.

Now you will use git to push changes to the remote version of your fork. 
- Begin by checking that there was a change using the `git status` command. You should see `main.py` in the list that is outputted.

- Now stage all of the changes by using the command `git add --all`.
- Create a commit with the command `git commit -m "Testing the CI/CD pipeline"`. 
- Finally push the changes using the command `git push origin main`.

With the push the CI/CD pipeline should have been triggered. To see it in action visit your forked repo in a browser and click the `Actions` button.


Here you will see all of the runs of the workflows you have set up. Right now you should see a run that looks like this (notice that the name is the same as the commit message):

![workflow-run](../../assets/workflow-run.png)

You can click on the name of this run to see a summary of the jobs that made it up. If you do so you will see there is only the job `test` that you defined in the `YAML` file:

![job](../../assets/job.png)

Now you can click once again the job to see a detailed list of all the steps of that job:

![steps](../../assets/steps.png)

Notice that these steps are the sames you defined in the configuration file plus some automatically added by GitHub.

This Action takes around 40 seconds to complete so by now it should have finished. Click again on the `Actions` button to see the list of workflow runs and you should see the run accompanied by a green icon showing that all tests passed successfully:

![good-run](../../assets/good-run.png)

You just run your own CI/CD pipeline! Pretty cool!

## Running the pipeline more times

### Changing the code

Suppose a teammate tells you that the Data Science team has developed a new model with an accuracy of 95% (the current one has 91%) so you decide to use new model instead. It is found in the `models/wine-95.pkl` file so to use it in your webserver you need to modify `main.py`. You should change the following lines:

```python
with open("models/wine.pkl", "rb") as file:
    clf = pickle.load(file)
```

So they look like this:

```python
with open("models/wine-95.pkl", "rb") as file:
    clf = pickle.load(file)
```

Once the change is saved, use git to push the changes as before. Use the following commands in sequence:

- `git add --all`
- `git commit -m "Adding new classifier"`
- `git push origin main`

With the push the CI/CD pipeline should have been triggered again. Once again go into the browser and check it. This time you will find that the tests failed. This can be done by the red icon next to the run:

![bad-run](../../assets/bad-run.png)

So, what happened?
You can dig deeper by going into the job and then into the steps that made it up. You should see something like this:

![error-detail](../../assets/error-detail.png)

The unit test failed because this new model has an accuracy lower to 90%. This happened because due to some miscommunication between teams, the Data Science team did not provide a `sklearn.pipeline.Pipeline` which first step is a `sklearn.preprocessing.StandardScaler`, but only the model since they expected the test data to be already scaled.

**Congratulations on finishing this ungraded lab!**

In this lab you saw what GitHub Actions is, how it can be configured and how it can be used to run CI/CD pipelines. This topic is very cool since it automates many repetitive processes such as running unit tests to ensure the quality of the software you are shipping.

These pipelines are meant to run really quickly so you can iterate your code in an agile and safe way.

**Keep it up!**
