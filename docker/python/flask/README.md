# Python Flask API runnig on Docker

## Summary

Example project of how to create a basic docker container running python flask in debug mode

## Getting Started

### Prerequists


### Building the container and running it

1. Ensure you have **docker installed** for your appropriate platform [here](https://www.docker.com/)
2. Open **terminal** or **cmd** prompt depending on the system your are running
3. **Run** the below **command**. This will build the image to run the docker container from

   `docker image build -t <replace_with_image_name> -f Dockerfile`

4. **Run** the below **command** to build a container from the image you created.

   `docker run -d -p 5000:5000 --name <my_container_name> <replace_with_image_name>`

5. You should now be able to reach the application with opening a browser and going to http://localhost:5000/ or you should be
able to do `curl http://localhost:5000/` from terminal

```json
{
    "status": 200,
    "message": "OK"
}
```