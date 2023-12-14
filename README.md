# Git and Github Assingment

Congratulation for successfully completed the Git and Github onboarding session. 🎉 

For this assingment, you need to create a simple application in order to practice the Git knowledge that you have learned. Practice make perfect, right?

> 🚨 Read the Objective before you go straight to the project details. 


## Objective

1. To implement the Git and Github knowledge in application development.
2. To implement [Git commit convention](https://www.conventionalcommits.org/en/v1.0.0/). 
2. To learn fundamentals of application deployment. 
3. To learn software engineer adaptation practices. 
4. To learn about Pull Request and code review. 
5. To implement [modularization](https://blog.inedo.com/python/modularization-and-packages/) and single responsibility design (SOLID).
6. To write a [well-documented](https://peps.python.org/pep-0257/) applications. 

## Streamlit App: MyCalculator

### Task
By using Streamlit framework, create an application that has basic calculator features. 

### Steps

1. **Fork** this repository and develop the code on it. 
2. Create a `virtual environment` and activate it before start installing project packages. [Read more](https://realpython.com/python-virtual-environments-a-primer/)

3. Develop calculator app should have the following features:

	* [ ] Addition feature- adding 2 numbers
	* [ ] Substraction feature- substracting 2 numbers
	* [ ] Division feature- dividing 2 numbers
	* [ ] Multiplication feature- multiplying 2 numbers

4. Deploy your apps on Streamlit Cloud.
5. Share the deployed apps URL in the Pull Request.

### Requirements

1. Your application should have **Titles** and necessary UI cosmetics.
	
2. Your repository should have the following file structure (you can add more necessary files):
	```
	onb_assingment/
		|-- README.md
		|-- .gitignore
		|-- LICENSE
		|-- requirements.txt
		app/
			|-- main_ui.py				
			|-- calculator.py			
			|-- utils.py			
	```
	|Files|Description|
	|--------|---------|
	|main_ui.py|user-interface (streamlit)|
	|calculator.py|backend function|
	|utils.py|helper function|
	|requirements.txt|list of libraries|

3. Your function or method line should be within your palm size. 
4. Your apps should use modularization by separating function into smaller size.s
5. Your function should have docstrings and necessary comments. 
6. Your application should be friendly user. 

## Goals

* [ ] Use Git Command
* [ ] Use git add, git commit, git push, git pull
* [ ] Implement modularization 
* [ ] Write well documented functions (dostring)
* [ ] Implement UI from Streamlit