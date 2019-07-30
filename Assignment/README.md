
# moneyflow-hello
This is repo acts as a template for the Moneyflow coding assignment.

## Prequisites
Ensure that you have docker and docker-compose installed.

For MacOS you can install with:
```
brew cask install docker
brew install docker-compose
```

## Run development server
To run the development server, simply bring the Docker containers online with:

```
docker-compose up
```

The development server is now online at `http://localhost:5000`


## Rebuild the image
If you change `requirements.txt` or the Dockerfiles themselves, you can rebuild the relevant image with:

```
docker-compose build django  # rebuild the django image
```

