#Run tests 

#Test the span covered by the tests
coverage run -m pytest -v

#Test the span covered by the tests and stops running at the first failed test
#coverage run -m pytest -x

#Gives a comprehensive coverage report as output
coverage report 
