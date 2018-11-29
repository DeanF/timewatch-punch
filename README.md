## Security note from the author
***The following links to herokuapps have been provided by 3rd parties, it is EXTREMELY recommended you host your own instance of this API.***

### Force me to click on buttons you shall not

http://timewatch.co.il is a simple (and annoying) web application given to employees to mark the time of their arrival and departure to/from work.  

The hassle of logging in every day and clicking on the "I'm here!" button made me look for an automated solution location based. crediting this awesome [blogpost](https://deanf.me/2017/02/24/automate-heroku-ifttt-maker/), and after some adjustments + fixes - it can be automated using the almighty [IFTTT](https://ifttt.com)  app


![image](https://user-images.githubusercontent.com/1287098/49186951-a5e4fd80-f36e-11e8-8a87-199093855d1b.png)

![image](https://user-images.githubusercontent.com/1287098/49186995-d167e800-f36e-11e8-82d4-84aafbf7fb16.png)



### Basic Usage

You'll only need 2 things
1. a mobile phone with the IFTTT app installed
1. credentials to http://timewatch.co.il


Login to IFTTT and create 2 new applets based on location, one for entering the place and one for leaving the place

- set the location with a decent radius

- set the url to `https://timewatch-ws.herokuapp.com/punch-out` or `https://timewatch-ws.herokuapp.com/punch-in`

- set the http method to `POST`

- set the content type to `application/json`

- set the body to

    ```json
    { "employeeId": "ZZZZ", "company": "YYYY", "password": "XXXX"}
    ```
    
#### Example

![image](https://user-images.githubusercontent.com/1287098/49187248-91553500-f36f-11e8-9f81-561f0bf93ac8.png)

