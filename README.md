# Stock Portfolio API
 **Authors**: Ben Hurst & Chris Turner
 **Version**: 1.0.0

 ## Overview
 Simple Kickstarter Display Using Django

 ## Getting Started
    1) Clone or fork repo from github.
    2) In the terminal, run ```docker-compose up --build```
    3) Once the docker container is running, in a separate terminal instance, run ```docker exec -it kickstarter_web bash``` and then ```python3 load_db.py```. This will take a minute or two.
    4) In the browser, go to ```0.0.0.0:8000```

 ## Architecture
Python 3.7, Django Web Framework, Docker, Postgresql
GitHub

 ## API

- **GET** / - the base API route

- **GET** /?page={page_number} - Paginator query strings.


 ## Change Log
 09-24-2018 16:50 Basic Scaffolding

 09-24-2018 18:30 Database Populating

 09-25-2018 17:50 Cache & pagination working

 09-26-2018 18:50 Styling

 ## License
This project is licensed under the MIT license
