pipeline {
    agent { docker { image 'maven:3.3.3' } }
    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    	stage('run') {
    		steps {
    			sh 'java -jar Rectangle.jar 7 9'
    		}	
    	}
    }
}
