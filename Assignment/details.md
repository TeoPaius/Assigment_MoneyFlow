To solve the requirement i have created an app call persons in django which contained 2 models

- persons
- friendships

1 friendship contains 2 persons

The post and delete methods for creating or removing a friendship are located at url **\friendships**

The first time the user enters the /friendships url, if the database is empty then it will generate some random samples