# DineSafe Toronto

A [datasette][datasette] of the [City of Toronto's DineSafe][dinesafe] data.

[datasette]: https://datasette.io/
[dinesafe]: https://www.toronto.ca/community-people/health-wellness-care/health-programs-advice/food-safety/dinesafe/

## Commands

### Scape DineSafe 

The `scrape-data` command will scrape the DineSafe JSON data and save it to a 
SQLite database.

```console
foo@bar:~$ poetry run dinesafe-toronto scrape-data dinesafe.db
```

## Develop

You'll need to have [Poetry][poetry], a Python packaging and dependency system,
installed. Once installed you can run:

```console
foo@bar:~$ make setup
```

[poetry]: https://python-poetry.org
