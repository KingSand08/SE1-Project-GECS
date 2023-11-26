pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('hw5') {
                    sh 'node --version'
                    sh 'npm --version'
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }
    }
}
