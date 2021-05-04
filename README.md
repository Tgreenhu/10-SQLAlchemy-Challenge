# 10-SQLAlchemy-Challenge

In this assignment, we were tasked with analyzing climates using a given SGLite database.

First, I using SQLAlchemy I brought in the database to my Jupyter Notebook for reflect on our data.  Using this data, I created a session query to grab all precipitation data from the last year of our data and created a DataFrame the view.  Using this DataFrame, I created a bar graph to give my data a visual.

![Screen Shot 2021-05-03 at 10 01 59 PM](https://user-images.githubusercontent.com/23372412/116953422-31a79600-ac5b-11eb-9a4b-d884feb9202d.png)

Using similar functions as above, I found the most active weather station in our database and found the following info:
    - Lowest temperature recorded
    - Highest temperature recorded
    - Average of all temperatures recorded
I also created a DataFrame to save the last year of temperature recordings to create a histogram, visualizing the data found.

![Screen Shot 2021-05-03 at 10 01 41 PM](https://user-images.githubusercontent.com/23372412/116953389-25bbd400-ac5b-11eb-9167-5d0340da3100.png)

Next, using Flask API I created an app with the following 5 routes:
    - Homepage
    - JSONified list of recipitation recordings & the dates
    - JSONified list of all stations and their information
    - JSONified list of the most active stations
    - JSONified list of the min, max, and avg temperature of a given range
        - if no end date given, use the most recent recording as the end date

![Screen Shot 2021-05-03 at 10 03 16 PM](https://user-images.githubusercontent.com/23372412/116953495-63206180-ac5b-11eb-9620-8ec8cf4cc17f.png)
