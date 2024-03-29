
## Colorize App


### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone git@github.com:jaypee15/colorize.git
```

--> Move into the directory where we have the project files : 
```bash
cd colorize
```

--> Create a virtual environment.:
```bash
# Create virtual env first
python -m venv .venv
```

--> Activate the virtual environment :
```bash
.venv\scripts\activate
```

--> Install the requirements :
```bash
pip install -r requirements.txt
```

--> Run Migrations
```
Python manage.py migrate
```

--> Run Tests 
```
python manage.py test 
```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver
```


> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Before
</p>
<img src="https://github.com/jaypee15/colorize/blob/main/static/preview/water-before.jpeg?raw=true">
</td> 
<td width="50%">
<br>
<p align="center">
  After
</p>
<img src="https://github.com/jaypee15/colorize/blob/main/static/preview/water-after.png?raw=true">  
</td>

<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Before
</p>
<img src="https://github.com/jaypee15/colorize/blob/main/static/preview/before-flower.jpg?raw=true">
</td> 
<td width="50%">
<br>
<p align="center">
  After
</p>
<img src="https://github.com/jaypee15/colorize/blob/main/static/preview/after-flower.png?raw=true">  
</td>
</table>

