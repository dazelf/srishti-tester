import requests

class Tester():
    def __init__(self,token, base_url,port:int=443) -> None:
        self.token = token
        self.base_url = base_url
        self.port = port
        self.session = requests.Session()
        self.headers = {
            "Authorization" : self.token, 
        }
        
        
    def check(self, response)->tuple[Exception|None,dict|None]:
        try:
            return None,response.json()
        except Exception as a:
            return a,None
        
     
    def get_all(self):
       """
       It makes request to this path
       /api/v1/data/
       and fetch all data related to that project
       Tester(...).get_all()
       """
       return self.check(self.session.request("GET",f"{self.base_url}:{self.port}/api/v1/data/",headers=self.headers))
       
       
    def get_table_data(self,table:str):
       """
       It makes request to this path
       "/api/v1/data/?table=table_name"
       and fetch all data related to that table
       Tester(...).get_table_data(table:table_name)
       """
       return self.check(self.session.request("GET",f"{self.base_url}:{self.port}/api/v1/data/",headers=self.headers))
       
       
    def get_data_by_id(self, id:int,table:str):
       """
       It makes request to this path
       "/api/v1/data/id/?table=table_name"
       and fetch all data related to that table
       Tester(...).get_data_by_id(id:id,table:table_name)
       """
       return self.check(self.session.request("GET",f"{self.base_url}:{self.port}/api/v1/data/{id}/?table={table}",headers=self.headers))
       
       
    def post(self,table:str,data:dict, files:dict|None = None):
        """
        It makes request to this path
        "/api/v1/data/?table=table_name"
        and store the data to the given table
        Tester(...).post(table:table_name,data:data)
        """
        return self.check(self.session.request("POST",f"{self.base_url}:{self.port}/api/v1/data/?table={table}",data=data, files=files, headers=self.headers))
        
        
    def put(self,id:int,table:str,data:dict,files:dict|None = None):
        """
        It makes request to this path
        "/api/v1/data/id/?table=table_name"
        and update the data related to the given of the given table
        Tester(...).put(id:id,table:table_name,data:data)
        """
        data['_method']='PUT'
        return self.check(self.session.request("POST",f"{self.base_url}:{self.port}/api/v1/data/{id}/?table={table}",data=data,files=files,headers=self.headers))
        
        
    def delete(self,id:int,table:str):
        """
        It makes request to this path
        "/api/v1/data/id/?table=table_name"
        and delete the data related to the given of the given table
        Tester(...).delete(id:id,table:table_name)
        """
        data = {
            '_method':'DELETE'
        }
        return self.check(self.session.request("POST",f"{self.base_url}:{self.port}/api/v1/data/{id}/?table={table}",data=data,headers=self.headers))
        
    
        
        