# learn_english_app
Django web application to keep organized your notes from English classes.

## Table of contents

* [Introduction](#-introduction)  
* [Installation and Launching](#-installation--launching)  
* [Contribution](#-contribution)  
* [License](#-license)  

## 👋🏠 Introduction

This Django web application aims to help creating organized PDF notes from hierarchical data obtained from the database.  
⚠️ Current project is ready only for a local environment, not production.  
⚠️ This project is under construction: database data must be provided manually and you can't apply filters to PDF generation right now. In the future, the idea is to be able to generate PDF notes related only to a certain label, for example.

## 🚀🧑‍🚀 Installation & Launching
1️⃣ - You'll need to have [Git](https://git-scm.com/) and your empty [Python](https://www.python.org/) environment.  

2️⃣ - Clone this repository with 
```shell
git clone https://github.com/Alejandro97JS/learn_english_app.git
```

3️⃣ - Install dependencies in your Python environment. In the same folder as the [_manage.py_](manage.py) file, execute 
```shell
pip install -r requirements.txt
```

4️⃣ - From [_.env.example_](.env.example), create your _.env.local_ file (you can simply rename it to begin with).  

5️⃣ - Execute the migrations:
```shell
python manage.py makemigrations
python manage.py migrate
```

6️⃣ - Create your superuser to log into de Django admin interface:
```shell
python manage.py createsuperuser
```

7️⃣ - Launch the application:
```shell
python manage.py runserver
```

8️⃣ - Log in via http://127.0.0.1:8000/admin and populate the table _Entrys_ of _Vocabulary Expressions_ with some example data.  

9️⃣ - Go to http://127.0.0.1:8000/pdf_generation/vocabulary_expressions and you will see the generated PDF with your data. The file will be saved, too.  

## 🪵🦫 Contribution
Of course, **contributions are very welcome**.  
Specially, a cool front-end would be an awesome contribution.
Please, feel free to contact me or to send your Pull Request.

## 📒📜 License
This repository is under a [MIT](./LICENSE) license.
