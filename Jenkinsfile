pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // echo 'Building.. Modified'
                git branch: 'main', url: 'https://github.com/ApriIrwansyah/test-automation-orangeHRM-pytest.git'
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
