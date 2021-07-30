<h1><u>Mars Mission</u></h1>
<hr>

![Mars](images/mars.jpg)
<hr>

### <u>Background</u>
The user needs an app, that scrapes various websites for data related to the Mission to Mars and shows the information in a HTML page.
<br>

The web pages that the user demand to make the scraping of are the following:
1. https://redplanetscience.com
<br>

![Mars](images/scrape1.png)
2. https://spaceimages-mars.com
<br>

![Mars](images/scrape2.png)
3. https://galaxyfacts-mars.com
<br>

![Mars](images/scrape3.png)
4. https://marshemispheres.com
<br>

![Mars](images/scrape4.png)

<hr>

### <u>Tools</u>
* Python
* BeautifulSoup
* Splinter
* Web Driver Manager
* Pymongo
* Mongo DB
* Jupyter Notebook
* Visual Studio Code

<hr>

### <u>How does the app work?</u>

#### <p>Installing Complements</p>

   - Installing Flask Pymongo
    * Code: pip install Flask-PyMongo
    ![Mars](images/mistake1.png)


   - Installing BeautifulSoup
    * Code: pip install beautifulsoup4
    ![Mars](images/mistake5.png)


   - Installing Splinter
    * Code: pip install Splinter
    ![Mars](images/mistake2.png)


   - Installing Web-Driver Manager
    * Code: pip install webdriver-manager
    ![Mars](images/mistake3.png)


   - Installing Lxml
    * Code: pip install lxml
    ![Mars](images/mistake4.png)

#### <p>Running the App</p>

1. Open your terminal so you can run your app. Run it with the following code "python 'name_of_your_app.py'", for example my app is called "mars_app.py", so to run the app, the code in the terminal will be: "python mars_app.py". If everything is working correctly the terminal will output a https address: "http://127.0.0.1:5000/"
![Mars](images/img3.png)
<br>

2. When you open the http address http://127.0.0.1:5000/ in the browser, the starting page will run a default scrape, and will store the values in the home page.
![Mars](images/img1.png)
<br>


3. To scrape new values so that the home page refresh, with new data, we need to click in the button: "Scrape New Data".

  ![Mars](images/img4.png)
<br>


4. When the user click on the "Scrape New Data" button, the program will make the calls and start scraping the selected web pages, and storing the information into a Mongo DB.
![Mars](images/img2.png)
<br>

  ![Mars](images/img6.png)
<br>


5. The data stored in Mongo DB will power the new html page, with images, texts, tables, and headlines.
![Mars](images/img5.png)
<br>





<hr>

### <u>Contact</u>
* Name: Raul Maya Salazar
* Phone: +52 833 159 7006
* E-mail: raulmayas20@gmail.com
* GitHub: https://github.com/RaulMaya
* LinkedIn: https://www.linkedin.com/in/raul-maya/
