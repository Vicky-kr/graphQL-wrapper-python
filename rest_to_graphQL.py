import requests
import graphene
import json

URL = 'https://jsonplaceholder.typicode.com/todos/'

try:
    #getting the json from the URL
    response = requests.get(url=URL)
    data = response.json()
    
    # Create a Todo Object
    class Todo (graphene.ObjectType):
        userId = graphene.Int()
        id = graphene.ID()
        title = graphene.String()
        completed = graphene.Boolean()

    # Create the Query
    class Query(graphene.ObjectType):
            todos = graphene.List(Todo,size = graphene.Int(default_value = -1))
            todo = graphene.Field(Todo,id=graphene.Int(default_value = 1))

            def resolve_todos(root,info,size):
                if size == -1:
                    return data
                else :
                    return data[:size]
            
            def resolve_todo(root,info,id):
                todo = None
                if id <= len(data):
                    start = 0
                    end = len(data) - 1
                    mid = (start + end) // 2
                    while (start < end):
                        if data[mid]['id'] == id :
                            todo = data[mid]
                            break
                        else:
                            if data[start]['id'] == id :
                                todo = data[start]
                                break
                            elif data[end]['id'] == id:
                                todo = data[end]
                                break
                            elif data[mid]['id'] < id :
                                start = mid
                            else:
                                end = mid
                            mid = (start + end) // 2

                return todo
    
    #Creating a schema
    schema = graphene.Schema(query=Query)

    query = '''
             query myQuery {
               todos {
                    id
                    title
                }
            }
    '''
    result = schema.execute(query)

    #Output Result 
    print(json.dumps(result.data,indent=3))
except Exception as e:
    print(e)