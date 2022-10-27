# Rasa task-oriented example

## Description

This bot is an example of task-oriented bot that developed with Rasa framework. Bot can retrieve intresting facts according to topic (e.g. about human or animals). Database was handcrafted and stores facts as key-value at `fake_db.json`. Bot requires topic using so called slot-filling (or form-filling) mechanism. To collect topic NLU uses lookup tables (rule based approach), but intent recognition solved by pretrained transformer LM and DIET on top it (machine learning approcah).

## Setup & run

It was developed for python 3.8.15

1. create and activate venv
```bash
# create
python -m venv venv

# if you use Ubuntu (or similar)
source venv/bin/activate 

# if you use Windows
venv\Scripts\activate.bat
```

2. install dependencies
```bash
pip install rasa==3.2.10
pip install transformers==4.13.0
```

3. train bot
```bash
rasa train
```

4. run action server

```bash
#shell_session_1
rasa run actions
```

5. run bot in shell

```bash
#shell_session_2
rasa shell
```



