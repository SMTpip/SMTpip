# SMTpip: A Tool for Resolving Dependency Conflicts in Python Projects

### Where to Find SMTpip

SMTpip is open-source and hosted on GitHub. You can access and download the tool from the following link:
`https://github.com/SMTpip/SMTpip.git`

### System Requirements

Ensure the following requirements are met before using SMTpip:

- **Python**: Version 3.8 or later.


### Installation Instructions

Follow these steps to install SMTpip on your system:

Step 1: Clone the repository.

```bash
git clone https://github.com/SMTpip/SMTpip.git
```

Step 2: Create a virtual environment.
```bash
python -m venv myenv

.\myenv\Scripts\activate
```
Step 3: Install the required dependencies

```bash
pip install -r requirements.txt
```
Step 4: Once installed, Extract the `KGraph.zip` and make sure the `KGraph.json` remains in the directory ".\SMTpip\" 

SMTpip is ready to use.


## How to Use SMTpip
There are 3 example Python projects named `example_python_project`. Each `example_python_project` folder contains a `program.py` and `requirements.txt` file.

###                 -----------------------Example 1-----------------------
The `requirements.txt` contains

```bash
click==6.6
pip-tools>=4.0.0
```

Now run the below command to input this `requirements.txt` into `SMTpip` to solve it.
```bash
python .\SMTpip.py -d .\example_python_project_1\
```
After running the command three files will be generated:
1. `install_script.txt` - Contains the resolved packages and their versions along with python version required.
```bash
# Specify Python version
python_version=="3.13.0"

# List of package dependencies
six==1.16.0
pip-tools==4.4.0
click==6.6
```

2. `execution_log.txt` - Contains the the time taken in each step of the program.

```bash
2025-10-16 21:33:53,631 - INFO - Input files successfully read.
2025-10-16 21:33:53,631 - INFO - Reading files execution time: 0.55 seconds
2025-10-16 21:33:53,631 - INFO - Parsing requirements execution time: 0.00 seconds
2025-10-16 21:33:53,644 - INFO - Fetching dependencies execution time: 0.01 seconds
2025-10-16 21:33:54,545 - INFO - Generating SMT expression execution time: 0.20 seconds
2025-10-16 21:33:54,577 - INFO - SMT expression saved to: .\example\SMT_expression.txt
2025-10-16 21:33:54,609 - INFO - Solving SMT expression execution time: 0.03 seconds
2025-10-16 21:33:54,624 - INFO - Solution saved to: .\example\log.txt
2025-10-16 21:33:54,634 - INFO - Generating install_script.txt execution time: 0.00 seconds
2025-10-16 21:33:54,634 - INFO - install_script.txt generated successfully.
```
3. `SMT_expression.txt` - Contains the SMT encoding for this example project. This file is generated to show our SMT encoding details.

#### Example 1 explaination:
A dependency conflict occurs because the project explicitly requires click==6.6, while pip-tools (≥4.0.0)—specifically its latest version 7.4.1—depends on click≥8.0. This transitive dependency creates an incompatibility. To resolve it, To resolve it, SMTpip finds a version of pip-tools without conflicts (here, pip-tools 4.4.0).


###                -----------------------Example 2-----------------------
The `requirements.txt` contains
```bash
oauthlib==2.*
jupyterhub>=0.8
```
Now run the below command to input this `requirements.txt` into `SMTpip` to solve it.
```bash
python .\SMTpip.py -d .\example_python_project_2\
```
After running the command three files will be generated:
1. `install_script.txt` - Contains the resolved packages and their versions along with python version required.
2. `execution_log.txt` - Contains the the time taken in each step of the program.
3. `SMT_expression.txt` - Contains the SMT encoding for this example project. This file is generated to show our SMT encoding details.

#### Example 2 explaination:
A dependency conflict occurs because the project explicitly requires oauthlib==2.*, while jupyterhub (>=0.8)—specifically its latest version 4.1.5—depends on oauthlib>=3.0. This transitive dependency creates an incompatibility. To resolve it, SMTpip finds a version of jupyterhub without conflicts (here, jupyterhub 0.9.1).

###                 -----------------------Example 3-----------------------
The `requirements.txt` contains
```bash
requests>=2.26.0 
googlesearch_python==1.1.0
```
Now run the below command to input this `requirements.txt` into `SMTpip` to solve it.
```bash
python .\SMTpip.py -d .\example_python_project_3\
```
After running the command three files will be generated:
1. `install_script.txt` - Contains the resolved packages and their versions along with python version required.
2. `execution_log.txt` - Contains the the time taken in each step of the program.
3. `SMT_expression.txt` - Contains the SMT encoding for this example project. This file is generated to show our SMT encoding details.


#### Example 3 explaination:
A dependency conflict arises because the project requires requests ≥ 2.26.0, while googlesearch-python == 1.1.0 depends on requests ≤ 2.25.1. This incompatibility stems from googlesearch-python’s transitive dependency on an older version of requests. SMTpip detects a dependency conflict and shows `Not satisfiable.`


###                 -----------------------Example 4-----------------------
The `requirements.txt` contains
```bash
idna>=3
click==6.6
requests==2.22.0
pip-tools<4.4.1
```
Now run the below command to input this `requirements.txt` into `SMTpip` to solve it.
```bash
python .\SMTpip.py -d .\example_python_project_4\
```
After running the command three files will be generated:
1. `install_script.txt` - Contains the resolved packages and their versions along with python version required.
2. `execution_log.txt` - Contains the the time taken in each step of the program.
3. `SMT_expression.txt` - Contains the SMT encoding for this example project. This file is generated to show our SMT encoding details.


#### Example 4 explaination:
A dependency conflict arises because the project requires idna>=3, while requests==2.22.0 depends on idna<2.9. This incompatibility stems from requests’ transitive dependency on an older version of idna. SMTpip detects a dependency conflict and shows `Not satisfiable`.
