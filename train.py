from vanna.remote import VannaDefault
vn = VannaDefault(model='projai', api_key='56c10509c96a415d83d95c089d156c35')
vn.connect_to_mysql(host='db-mysql-sgp1-proj-ai-dev-do-user-11333017-0.g.db.ondigitalocean.com', dbname='election', user='doadmin', password='AVNS_VsqqAPzLMCSlHjSg8ME', port=25060)

#train plan
df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")
plan = vn.get_training_plan_generic(df_information_schema)
id = vn.train(plan=plan)

#remove training data
#td = vn.get_training_data()
# print( type(td))
# for index, row in td.iterrows():
#     print(row['id'])
#     vn.remove_training_data(id=row['id'])

