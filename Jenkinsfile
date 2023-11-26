pipeline {
    agent any // Use a non-Docker agent

    stages {
        stage('Build Svelte App') {
            steps {
                dir('hw5') {
                    // Ensure Node.js and npm are installed on the agent
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }
    }
}
