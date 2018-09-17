pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                /*sh 'sudo pip install -U pytest'*/
                sh 'pytest --junitxml=tests/results.xml'
                /*sh 'ant -f test.xml -v'
                junit 'reports/result.xml'*/
            }
        }
        stage('Setup') {
            steps {
                echo "Building and Installing Sandman"
                sh 'python -u mathlib.py'
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
            archiveArtifacts artifacts: 'tests/*.xml', fingerprint: true
        }
    }
}