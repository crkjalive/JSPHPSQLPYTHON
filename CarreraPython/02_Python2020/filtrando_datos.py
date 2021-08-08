DATA = [
	{
		'name':'Wizard',
		'age':37,
		'company':'Platzi',
		'position':'Backend',
		'language':'Python',
	},
	{
		'name':'Dexter',
		'age':36,
		'company':'Google',
		'position':'Data',
		'language':'Php',
	},
	{
		'name':'Linda',
		'age':39,
		'company':'Platzi',
		'position':'Soport',
		'language':'CSS',
	},
	{
		'name':'Jared',
		'age':2,
		'company':'Google',
		'position':'full stack',
		'language':'Kotlin',
	},
	{
		'name':'Leonardo',
		'age':37,
		'company':'Facebook',
		'position':'Frontend',
		'language':'Java',
	},
	{
		'name':'Nicolas',
		'age':37,
		'company':'Youtube',
		'position':'Underground',
		'language':'Python',
	},
	{
		'name':'Angie',
		'age':28,
		'company':'Youtube',
		'position':'Frontend',
		'language':'Javascript',
	},
	{
		'name':'Daniela',
		'age':26,
		'company':'Platzi',
		'position':'Backend',
		'language':'Python',
	},
]

def run():

	all_python_devs = [worker["name"]for worker in DATA if worker["language"]=="Python"]
	for worker in all_python_devs:
		print(f"devs of Python {worker}")

	all_platzi_devs = [worker["name"]for worker in DATA if worker["company"]=="Platzi"]
	for worker in all_platzi_devs:
		print(f"of platzi company {worker}")

	adults30 = list(filter(lambda worker: worker['age']<30, DATA))
	adults30 = list(map(lambda worker: worker["name"], adults30))
	for worker in adults30:
		print(f"adultos menores de 30 {worker}")


	old_people = list(map(lambda worker: worker | {"old": worker["age"] >= 30}, DATA))
	for worker in old_people:
		print(worker)








if __name__ == '__main__':
	run()