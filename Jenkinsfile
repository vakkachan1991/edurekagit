pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the source code from the current branch
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                // Install dependencies
                sh 'python3 -m pip install --upgrade pip'
            }
        }
        stage('Run Python Script') {
            steps {
                // Run the Python script
                sh 'python3 hello.py'
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests using unittest
                sh 'python3 -m unittest discover'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
