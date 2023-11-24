/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'node:20.9.0-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build Svelte App') {
            steps {
                dir('hw5') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }
    }
}