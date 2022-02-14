# GraphQL-wrapper-python
### This is to demonstrate how to convert a simple [REST API](https://restfulapi.net) to [GraphQL](https://graphql.org) in python using [Graphene](https://graphene-python.org)
<!-- ![alt text](https://the-guild.dev/blog-assets/migrating-from-rest/cover.png) -->
<img src = "https://the-guild.dev/blog-assets/migrating-from-rest/cover.png" height = "370" width = "700"/>

### For this project we are using [{JSON} Placeholder](https://jsonplaceholder.typicode.com) todo list api 

#### If we make a get request to [this link](https://jsonplaceholder.typicode.com/todos/) we get response like
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  }
  ....
]
```
###### Since there is no functionality to get a certain data such as first 10 datas or only the title and id of the todo tasks so we are left with either ignore those data or make an extra endpoint. But using GraphQL if we want to get a particular data we make __query__ as shown below to get the same result : 

```
query myFirstQuery {
  todos {
    userId
    id
    title
    completed
  }
}
```
##### Additionally if we want the first 2 tasks and only want the title and status of the task we make __query__ as shown below :

```
query mySecondQuery {
    todos (size:2){
        title
        completed
    }
}
```
#### In return we get response like this 

```json
[
  {
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  }
]
```
### Advantages of GraphQL over REST 
    - We only get those data what we query for
    - Helps in avoiding version control and creation multiple endpoints such as "baseURL/api/v2/"
    - Takes the shortest distance to retrieve the data hence faster than REST api
    - Since only required data is sent so it also increases the bandwidth of the websites (using GraphQL)

