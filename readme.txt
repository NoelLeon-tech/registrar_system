Before starting, ensure that you have the following prerequisites installed on your system:

Python (version 3.6 or higher)
Pip (Python package installer)
vs code

Step 1: Create a Virtual Environment (optional but recommended)
On macOS and Linux:
source myenv/bin/activate

On Windows:
myenv\Scripts\activate

Step 2:
Install Django using pip by running the following command:
pip install django

Step 3:
open cmd and go to the directory of your project
cd MyProject

Step 4:
To start the Django development server, run the following command:
python manage.py runserver

Step 5:
For Admin site:
Open your browser and type http://127.0.0.1:8000/admin/
user: admin
pass: admin

User site:
to create queue
http://127.0.0.1:8000/new_queue

to display queue
http://127.0.0.1:8000/queue_list
