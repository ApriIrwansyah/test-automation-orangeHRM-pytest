pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // echo 'Building.. Modified'
                git branch: 'main', url: 'https://github.com/username/repository.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing.. Modified'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.... Modified'
            }
        }
    }
}
