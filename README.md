# Rotten Tomato Rating


## How to run Rotten Tomato Rating program

### Envoiromet creation

1. Create your apikey on site from link below:
    `https://www.omdbapi.com/apikey.aspx`

2. Download repository and create `.env` file with parametes like in `.env_example` file.

3. Replace `<YOU_API_KEY>` with your api key received from www.omdbapi.com service.

4. Create Python virtual env using command: 
    ```
    python3 -m venv tutorial-env
    ```

5. Install all python packages by typing: 
    ```
    pip install -r requirements.txt
    ```

### Launching Docker conteiner

6. Run the following command from the same directory where the docker-compose.yml file is located.
    ```
    docker compose up
    ```

7. Now run `docker ps` to see all the running containers.

8. Now you can run the following command to see the files.__
    ```
    ls  
    Dockerfile   README.md   app.py   config.py   docker-compose.yml   requirements.txt
    ```

9. Access the running container `rottentomatoraiting_app_1` by running the following command:
    ```
    docker exec -it rottentomatoraiting_app_1 bash
    ```

### Runing Rotten Tomato Rating program

10. Run app by typing:
    ```
    python app.py --title <TITLE>` or `python app.py -t <TITLE>
    ```

11. For help run:
    ```
    python app.py --help` or `python app.py -h
    ```