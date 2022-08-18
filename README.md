# microservice-python-flask-sqlite

We will build a **Python Flask Rest CRUD API** for a **Todo Task Application** in that:

- Each **Todo Task** has *id, title, description, creation date, due date, status and comments*.
- APIs help to *Create, Read, Update, Delete* **Todo Tasks**.

Below mentioned are the ***REST APIs*** for CRUD Operations.

| Description | CRUD Operation  | HTTP Method | REST API Endpoint |
|:-----------:|:--------------:|:-----------:|:-----------------:|
| Create New Todo Task | CREATE | POST | `/todo-app/tasks/` |
| Fetch All Todo Tasks | READ | GET | `/todo-app/tasks/` |
| Fetch One Todo Task | READ | GET | `/todo-app/tasks/{id}` |
| Update One Specific Todo Task | UPDATE | PUT | `/todo-app/tasks/` |
| Delete One Specific Todo Task | DELETE | DELETE | `/todo-app/tasks/{id}` |
| Delete All Todo Task | DELETE | DELETE | `/todo-app/tasks/` |

**Python Flask Framework** will serve as back-end server and I will be using ***Relational Database*** known as **SQLite Database**, for persisting(storing) the data.

## Requirements

### Install Python 
Install latest version for your platform from [here](https://www.python.org/downloads/windows/). Select the latest version of **Python 3** and download the Windows Installer. Click on the downloaded *.exe* and follow the on-screen instructions to complete the download.

### Integrated Development Environment (IDE) for Code Development
You can use any Text Editor or IDE of your choice. I will be using the **Visual Studio Code**.

If you wish to use the **Visual Studio Code**, download the latest version from [here](https://aka.ms/win32-x64-user-stable). Click on the downloaded *.exe* and complete the installation.

### Install the Python Extension for the VS Code
Install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Visual Studio Marketplace.
1. You can browse and install extensions from within VS Code. Bring up the Extensions view by clicking on the *Extensions icon* in the **Activity Bar** on the side of VS Code or the **View: Extensions** command (`Ctrl+Shift+X`).
2. Browse for **Python** and click on **Install** button.

## Running the application locally

Run this Python application on your local machine by following below steps:

```shell
git clone https://github.com/prasbhat/microservice-python-flask-sqlite.git
cd microservice-python-flask-sqlite
py -3 -m venv .venv
.venv\Scripts\activate
flask run --port 8080
```

More detailed documentation regarding this project can be found [here](https://myzonesoft.com/post/microservice-python-flask-sqlite/).