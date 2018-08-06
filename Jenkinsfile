pipeline {
	agent any
	stages {
		stage('build') {
			steps {
				sh 'javac -d . src/*.java'
			}
		}
	}
}