from srishti_tester.tester import Tester
# from dotenv import load_env
#TOKEN=load_env(ACCESS_TOKEN)

a = Tester(token="",base_url='http://localhost', port=8000)

files = {'image': open('example.jpg','rb')}

response = a.put(table="test_table", id=4, files=files, data={'name':'John', 'email':'test@test.com','password':'12345678'})

print(response)