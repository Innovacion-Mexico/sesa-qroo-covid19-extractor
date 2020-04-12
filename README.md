[![](https://images.microbadger.com/badges/version/etejeda/sesa-qroo-covid19-extractor.svg)](https://microbadger.com/images/etejeda/sesa-qroo-covid19-extractor "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/etejeda/sesa-qroo-covid19-extractor)
![GitHub top language](https://img.shields.io/github/languages/top/Innovacion-Mexico/sesa-qroo-covid19-extractor)
![GitHub last commit](https://img.shields.io/github/last-commit/Innovacion-Mexico/sesa-qroo-covid19-extractor)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Extractor Metrics From Sesa Official Webpage
A simple solution to extract and save all the metrics from the official website of SESA (State Health Services) of Quintana Roo, Mexico.

Visit also [docker hub repository](https://hub.docker.com/repository/docker/etejeda/sesa-qroo-covid19-extractor).

## How works?

Basically the information is extracted with the 'BeautifulSoup' utility using html, and then it is deposited in a postgresql database with the help of the ORM peewee.

## Requirements

* Docker Engine (for running container version ). :heart:
* Python3 (peewee, urlrequest, beatifulsoup, dotenv)
* PostgresSQL Database

## Getting Started

### Standalone

You only run this command in your terminal:

```
docker run \
-e DATABASE=${env.DATABASE} \
-e DB_USER=${USERNAME} \
-e DB_PASSWORD=${PASSWORD} \
-e DB_HOST=${env.DB_HOSTNAME} \
-e URL_SESA=${env.URL_SESA} etejeda/sesa-qroo-covid19-extractor:latest
```

or just create a file naming `.env` and put the env vars inside:

```
DATABASE=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=5432
URL_SESA=https://salud.qroo.gob.mx/portal/coronavirus/coronavirus.php
```

and then run the container in your terminal:

```
docker run --env-file YOUR-ENV-FILE etejeda/sesa-qroo-covid19-extractor:latest
```
### Schedule task

#### Jenkins

For more security, first add the user & password of db like secrets (like secret username/password) and then you need add a step in your pipeline executing the container image, example:

```
pipeline {
    agent any
    triggers {
        cron('H/15 * * * *')
    }
    environment {
        DATABASE = ''
        DB_PORT = '3306'
        DB_HOSTNAME = ''
        URL_SESA = 'https://salud.qroo.gob.mx/portal/coronavirus/coronavirus.php'
        CREDENTIALS = ''
    }
    stages {
        stage('Update DB') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.CREDENTIALS, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh " docker run -e DATABASE=${env.DATABASE} \
                        -e DB_USER=${USERNAME} \
                        -e DB_PASSWORD=${PASSWORD} \
                        -e DB_HOST=${env.DB_HOSTNAME} \
                        -e URL_SESA=${env.URL_SESA} etejeda/sesa-qroo-covid19-extractor:latest"
                }
            }
        }
    }
}
```

## Development
### Building the container

I provided a makefile for do this job, only run this command:
```
make run build 
```

### Environment Variables 

| Name  | Description  | Default | Required |
| -- | -- | -- | -- |
| DATABASE| Database name | - | *yes* |
| DB_USER | Username of database | - | *yes* |
| DB_PASSWORD | Password for database | - | *yes* |
| DB_HOST | Hostname or IP for the database | - | *yes* |
| DB_PORT |  Port number for the database | `5432` | no |
| URL_SESA | The current url for extract all metricts (SESA webpage) | - | *yes* |

## How contribute? :rocket:

Please feel free to contribute to this project, please fork the repository and make a pull request!. :heart:

## Share the Love :heart:

Like this project? Please give it a ★ on [this GitHub](https://github.com/Innovacion-Mexico/sesa-qroo-covid19-extractor)! (it helps me a lot).

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

See [LICENSE](LICENSE) for full details.

    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

