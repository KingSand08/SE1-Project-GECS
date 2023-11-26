/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'node' } }
    stages {
        stage('Build') {
            steps {
                dir('hw5') {
                    // Ensure Node.js and npm are installed on the agent
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
