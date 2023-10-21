## Python solution for BuzzSolutions Challenge using Fastapi and MySql

### Challenge #1

Design an API endpoint that provides autocomplete suggestions for large cities.
The suggestions should be restricted to cities in the USA and Canada with a population above 5000 people.

- the endpoint is exposed at `/suggestions`
- the partial (or complete) search term is passed as a query string parameter `q`
- the caller's location can optionally be supplied via query string parameters `latitude` and `longitude` to help improve relative scores
- the endpoint returns a JSON response with an array of scored suggested matches
  - the suggestions are sorted by descending score
  - each suggestion has a score between 0 and 1 (inclusive) indicating confidence in the suggestion (1 is most confident)
  - each suggestion has a name which can be used to disambiguate between similarly named locations
  - each suggestion has a latitude and longitude
- all functional tests should pass (additional tests may be implemented as necessary).

#### Sample responses

These responses are meant to provide guidance. The exact values can vary based on the data source and scoring algorithm.

**Near match**

    GET /suggestions?q=London&latitude=43.70011&longitude=-79.4163

```json
{
  "suggestions": [
    {
      "name": "London, ON, Canada",
      "latitude": "42.98339",
      "longitude": "-81.23304",
      "score": 0.9
    },
    {
      "name": "London, OH, USA",
      "latitude": "39.88645",
      "longitude": "-83.44825",
      "score": 0.5
    },
    {
      "name": "London, KY, USA",
      "latitude": "37.12898",
      "longitude": "-84.08326",
      "score": 0.5
    },
    {
      "name": "Londontowne, MD, USA",
      "latitude": "38.93345",
      "longitude": "-76.54941",
      "score": 0.3
    }
  ]
}
```

**No match**

    GET /suggestions?q=SomeRandomCityInTheMiddleOfNowhere

```json
{
  "suggestions": []
}
```

### Non-functional

- Mitigations to handle high levels of traffic should be implemented.
- Challenge is submitted with all the necessary files (code, scripts, dataset, readme, etc.) in a .zip folder
- Documentation and maintainability is a plus.

## Dataset

You can find the necessary dataset along with its description in the files attached.
Data -> cities_canada-usa.tsv
Description – README.md

## Getting Started

Begin by cloning this repo.

#### Obs: This project uses pyton 3.11, and was first developed in a linux enviroment

### Setting up the project

In the project root directory run

```
docker-compose up -d
```

After build the app and the database run the migrations

```
make migrate
```

When the migration is finished, run the script to populate the database

```
make populate
```

### Running the tests

The test cases can be runned with

**Obs: if your tests are not running, stop the docker and delete `mysql_data` directory**

```
make test 
```

or

```
make test-coverage
```



### Starting the application

To start a local server run

```
make run
```

which should produce output similar to

```
INFO:     Started server process [22804]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**Obs: the next step would be add a cache layer to the suggestions endpoint, caching the requests**
