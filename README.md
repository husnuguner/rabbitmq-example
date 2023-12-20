# Installations

All the below commands should be executed in the root directory of the project.

### RabbitMQ Installation with Docker
```bash
docker-compose up -d
# or
docker-compose -f docker-compose.yml up -d
```

### Python Environment Installation

#### Install Virtualenv
```bash
pip install virtualenv
````
#### Check Virtualenv Version
```bash
virtualenv --version
```
#### Create Virtualenv
```bash
virtualenv venv
```
#### Activate Virtualenv
```bash
venv\Scripts\activate
```
#### Install Requirements
```bash
pip install -r requirements.txt
```
#### Install Project
```bash
pip install -e . 
```

