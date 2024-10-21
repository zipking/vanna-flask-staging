from vanna.remote import VannaDefault

class MyVanna(VannaDefault):
  def __init__(self, model, api_key):
    VannaDefault.__init__(self, model=model, api_key=api_key)

  def generate_query_explanation(self, sql: str):
    my_prompt = [
        self.system_message("You are a helpful assistant that will output map of state of Malaysia as json"),
        self.user_message("State: " + sql),
    ]

    return self.submit_prompt(prompt=my_prompt)

vn = MyVanna(model='projai', api_key='56c10509c96a415d83d95c089d156c35')
vn.connect_to_mysql(host='db-mysql-sgp1-proj-ai-dev-do-user-11333017-0.g.db.ondigitalocean.com', dbname='election', user='doadmin', password='AVNS_VsqqAPzLMCSlHjSg8ME', port=25060)

test = vn.generate_query_explanation("Johor")
print(test)