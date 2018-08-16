pipeline {
    agent { docker { image 'maven:3.3.3' } }
    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
        stage("Promote Development Branch to Master") {
            agent {
                node {
                    label 'Test'
            }
            when {
                branch 'development'
            }
            steps {
                echo "Stashing Any Local Changes"
                sh 'git stash'
                echo "Checking Out Development Branch"
                sh 'git checkout development'
                echo "Checking Out Master Branch"
                sh 'git checkout master'
                echo "Merging Development into Master Branch"
                sh 'git merge development'
                echo "Pushing to Origin Master"
                sh 'git push origin master'
                }
            }
        }
    }
}