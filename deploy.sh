docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker container run -d -p 5000:5000 sergiomos/web-notes-api:v1.0.0
docker container run -d -p 80:8080 sergiomos/web-notes-app:v1.0.0
