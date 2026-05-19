This is real usecase request flow step-by-step for DRF:  
browser → server → database → response.  
My stack: 
- front end is Bootstrap
- back end is Django with Django REST Framework (DRF)
- database is Postgres
### Full Request Flow
Scenario:  
A user visits your barter platform and clicks on “Show available dog walks” button.  
How the frontend gets data from Django?  
1️⃣ Browser Loads the Page..
The user opens:

    https://dogswingers.com/walks/

Django serves an HTML page walks.html using Bootstrap.  

        <div id="walk-list"></div>
        
        <script>
        fetch('/api/walks/')
          .then(response => response.json())
          .then(data => {
              console.log(data)
          })
        </script>
At this point:
- Bootstrap handles styling
- JavaScript requests data from your API  

2️⃣ Browser Sends API Request 2 the Django backend
 
    HTTP request:
    GET /api/walks/

