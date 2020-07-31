Logboek Steven Verkest

27/8  -> could not work due to sickness

28/8  -> before noon -> make front-end with flask (make form to ask for user input with street , adress, number, postalcode)
      -> afternoon -> finish the front-end, and try to put user input into SQLlite-database 
			(decided to skip this because did not wanted to waste to much time on a nice-to-have
      problems: can't install progreSQL (installed slqlite)

29/8  -> before noon: prepare tech talk
      -> afternoon:-> put tif files into database (error import georasters) + trying http with Wim
      problems -> installing georasters did not work, costed lot of time

30/8  -> before noon: trying HTTP with Wim ( because maybe there is a better way instead of using a database)
      -> afternoon: try to putt the tiff-files into the database (geotiff->df->csv->database)
      problems -> installing docker & running an image did not work

31/8  -> before-noon -> try to put all csv files into database (not totally ready, but skipped due to time management)
      -> before-noon ->try to acces database with sqlalchemy (due to time management, changed plan to deploy app working with only 1 tile on docker & heroky
      -> before-noon -> try to put the database & python into docker (failed)
      -> afternoon try to make app run on heroku 
      problems -> installing docker (worked out after updating my windows and using docker (not fixed)
      problems -> getting the project done in time, trying to time manage the most important parts
      problems -> errors with deploying on heroku (lot of different errors, solved some of them, but at the end did not succeed to make it run like it should


ORIGINAL PLAN
-> make flask front end form to ask user input, and safe that in postgresSQL database
-> convert geotiffs to dataframes so they can be converted to csv's that i can insert into the database in an automated way
-> make sqlalchemy connect to the database so i can query from it, and then reverse engineer from datatabase rows to the geotiff again
-> put the database in a docker container
-> deploy the app on heroku

ACTUAL RESULT
-> make flask front end form to ask user input
-> convert geotiffs to dataframes so they can be converted to csv's, worked with a few csv files
-> make the app work with the csv locally in a folder (no database)
-> docker & heroku did not work

----------------------------------------------------------------------------------------------------------------------------------------------------
Logbook Wim Christiaansen

I've been exploring following subjects:

heroku (getting started, requirements, procfile,... did a successful deployment of an app, but always getting error when trying to view) 
docker (first windows issue, then after windows update and install struggling to make it work (daemon error))
pythonanywhere (tried this approach, to host a flask app, errors all around)
http.server (trying to serve tif files via local server, requesting the files in python code did not work)
