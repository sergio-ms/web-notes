docker image build -t web-notes-api:v1.0.0 .
docker tag web-notes-api:v1.0.0 sergiomos/web-notes-api:v1.0.0
docker push sergiomos/web-notes-api:v1.0.0