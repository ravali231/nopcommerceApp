#chrome
#pytest -rA -m "sanity or regression" --html=./Reports/report2.html testCases/ --browser=chrome
#rem pytest -rA -m "sanity and regression" --html=./Reports/report2.html testCases/ --browser=chrome
#rem is for comments in bat files
#pytest -rA -m "regression" --html=./Reports/report2.html testCases/ --browser=chrome
pytest -rA -m "sanity" --html=./Reports/report3.html testCases/ --browser=chrome

#firefox
#pytest -rA -m "sanity or regression" --html=./Reports/report2.html testCases/ --browser=firefox
#pytest -rA -m "sanity and regression" --html=./Reports/report2.html testCases/ --browser=firefox
#pytest -rA -m "regression" --html=./Reports/report2.html testCases/ --browser=firefox
#pytest -rA -m "sanity" --html=./Reports/report4.html testCases/ --browser=firefox

