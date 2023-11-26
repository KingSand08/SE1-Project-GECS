pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('hw5') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }
        stage('Test') {
            steps {
                dir('hw5') {
                    sh 'npm run test'
                }
            }
            post {
                always {
                    junit 'hw5/test-results.xml'
                }
            }
        }
    }
}
