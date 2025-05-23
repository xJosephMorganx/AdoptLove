# ADOPT LOVE
#### Video Demo:  <https://youtu.be/O3sOeetajDY>
#### Description:
***Hola mundo!***

My name is José Luis Gómez Sánchez and I am from Guadalajara, Mexico.

I had two reasons for deciding to create this project. First, after working on pset 9, I felt comfortable using Flask (my second favorite topic in the course, just after databases). Second, because in the part of the city where I live, there is a severe problem with stray dogs. I have adopted 3 dogs so far, but due to my financial constraints, I don't think I can adopt more at the moment. That's why I decided to create a web application to facilitate adoption, both for those who want to put a dog up for adoption and for those who want to adopt a dog.

I decided to do it in Visual Studio standalone app because I wanted to remove the training wheels from CS50.

I named this web app “Adopt Love,” and although the frontend is quite simple, since CS50 was my first experience writing code, it was quite challenging to create it from scratch. I decided to draw inspiration from pset 9, specifically from “finance.”

I started with the basics from my perspective: creating an app.py. I began by importing the libraries I thought were necessary: Flask for importing the classes and functions needed to create a web application with Flask, sqlite3 for interacting with SQLite databases, and OS for interacting with the operating system, in this case, for handling file paths.

Next, I created the Flask application instance and configured the folder where images uploaded by users who post their dogs for adoption will be stored.

Thanks to the fact that I am currently taking a database class at the university, this part was one of the simplest for me. After creating a database named dogs.db, I defined a function to create a table called dogs, where I included an auto-incrementing ID, the dog’s name, the dog’s age, a photo, the dog's owner's name, the owner’s contact email, and a timestamp using the current date.

![app1](/assets/images/image1.png)

Then, I decided to create a Jinja2 template called “base.html.” Here, I declared the doctype and the basic HTML tag, followed by the header where I used metadata, in this case, UTF-8, which includes most characters from all languages. I configured the viewport to be responsive, ensuring the design adjusts correctly on different screen sizes, and set the page title, which appears on the browser tab. I also linked an external CSS stylesheet to format the page and added a Flask function that generates the correct URL for the CSS file in the static folder.

I also decided to create an extremely simple navigation menu that only features a heart logo with a dog paw in the middle, which, when clicked, takes you to the index.

![base template](/assets/images/image2.png)

Returning to app.py, I added the route for the main page, calling it “index.html,” a route for the page with a form to post a dog for adoption, named “post_dog.html,” a route for the page where you can view the dogs that have been registered for adoption, called “feed.html,” and a route for another page where, after selecting a dog you want to adopt, it shows the owner’s name and contact email.

![app2](/assets/images/image3.png)

In index.html, I used the base template and, within the block, simply provided a brief welcome message, a subtitle explaining what the page is for, and two buttons: one to view the dogs available for adoption and another to fill out a form to post a dog for adoption.

![Index](/assets/images/image4.png)

For post_dog.html, I again used the base template and created a form with a text input for the dog's name, a numeric input for the dog’s age, a file input to upload the dog’s photo, two checkbox inputs to specify if the dog can get along with other dogs and if it is good with small children, another text input for the owner's name, an email input for the owner's contact email, and finally a button to submit the form. I added IDs for all these fields to link them to the database.

![post_dog](/assets/images/image5.png)

For feed.html, I used the Jinja2 template again, starting a loop that iterates over a list of dogs (dogs) and stores each element in a variable named “dog” during each iteration. Inside the loop, I created a container for each dog in the list, then displayed a picture of the dog by generating a URL for each image, provided text for the dog’s name, and indicated whether the dog can get along with other dogs and if it is compatible with small children. This text is dynamic: if the response is positive, it is shown in green, and if negative, in red. It shows the dog’s age, preceded by the label "Age:", and finally generates a URL to view the owner’s contact information in the “adopt.html” template.

![feed](/assets/images/image6.png)

I also created a CSS file to style everything above, although I kept it quite simple. I used Arial font and a white background, adding a touch of color by making the navigation bar magenta and including the previously described logo. I also used a container for the form and the feed and changed the headers to magenta.

I genuinely enjoyed working on this project as it is something I am passionate about. However, before putting it online, I would like to implement a method to keep track of adopted dogs and ensure they are being treated responsibly. I hope to implement this feature in the future, but for now, I believe, it is a good foundation to continue working on.
