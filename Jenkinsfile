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