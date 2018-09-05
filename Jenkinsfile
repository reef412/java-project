pipeline {
    agent any

    stages {
        stage('Unit Tests') {
            steps {
                sh 'sudo pip install -U pytest'
                sh 'pytest --junitxml=tests/results.xml'
                /*sh 'ant -f test.xml -v'
                junit 'reports/result.xml'*/
            }
        }
        stage('Setup') {
            steps {
                echo "Building and Installing Sandman"
            }
        }
        stage('Independent Tests') {
            steps {
                echo "Running Unit and Integration Tests"
            }
        }
        stage('Deploy') {
            steps {
                echo "Starting Sandman"
            }
        }
        stage('Dependent Integratinon Tests') {
            steps {
                echo "Running Dependent Integration Tests"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dist/*.txt', fingerprint: true
        }
    }
}