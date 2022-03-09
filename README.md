# django-inventory


<h3>The project has been set up to run on top of docker. </h2>

First, clone the repository and go to the cloned directory.

Please check whether ports 8000 and 5432 are free before running the docker instance.

Project can be started using following command.

`docker-compose up -d`

This will run in the background. The progress can be checked using following command.

`docker-compose logs -f`

Once the project build finishes, run the following command to apply the migrations.

`docker-compose run server python manage.py migrate`

Migration also contains the superuser creation. The following credentials can be used to log in as superadmin.

`username: admin`
`passowrd: admin`