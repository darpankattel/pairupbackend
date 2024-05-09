
# Pair Up

## Introduction
Pairup is a platform or system where users can collaborate based on their complementary skills, with the understanding that any profits generated from their joint efforts will be shared. It provides an opportunity for individuals with different skill sets to work together towards a common goal, leveraging their respective strengths to potentially create something profitable. And even if the project doesn't yield profits, it still serves as valuable experience and a portfolio piece for both parties involved. This is a backend project, built using Django, and DRF.

## Features
- Project enrollment, and partnership
- Social media platform

## Setup
To set up the project, follow these steps:

+ Clone the repository from GitHub:
```bash
git clone https://github.com/darpankattel/pairupbackend.git
```
+ Navigate to the project directory:
```bash
cd pairupbackend
```
+ Compose the project using Docker:
You must obvioulsy install docker or dockerhub or docker as a service as per your OS.
```bash
docker-compose up
```
Now, the project is running. PostgreSQL is running on port 5432:5432. The Django development server is running on port 8000:8000. For more information on the project, view the Dockerfile and the docker-compose.yml files.

## Without Docker
To set up the project without Docker, follow these steps:
+ Clone the repository from GitHub:
```bash
git clone https://github.com/darpankattel/pairupbackend.git
```
+ Navigate to the project directory:
```bash
cd pairupbackend
```
+ Create a virtual environment:
```bash
python -m venv venv
```
+ Activate the virtual environment:
For Linux:
```bash
source venv/bin/activate
```
For Windows:
```bash
venv\Scripts\activate
```

+ Install the required dependencies:
```bash
pip install -r requirements.txt
```
+ Run the project: 
```bash
python manage.py runserver
```