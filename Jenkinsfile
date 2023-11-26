/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'node' } }
    stages {
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