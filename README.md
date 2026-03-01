## this repository is to help me to learn Python backend framework - Django. 
The materials I've used: 
Learn Django: https://www.w3schools.com/django/index.php  

How Django works: 

    - Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
    - The view, located in views.py, checks for relevant models.
    - The models are imported from the models.py file.
    - The view then sends the data to a specified template in the template folder.
    - The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.
Django Model View Template design pattern:  

    - Model - The data you want to present, usually data from a database. Located in models.py
    - View - A request handler that returns the relevant template and content - based on the request from the user. Located in view.py
    - Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.  
      Located in a folder named templates
    - To navigate around the different pages in a website. When a user requests a URL, Django decides which view it will send it to. Its done in a file  urls.py


