/*pipeline {
    
     agent any 
     stages {
        stage ('Compile Stage') { 
             
                 steps {
                 withMaven(maven : 'maven_3_6_3') {
                 sh 'mvn clean compile'
                 
                 }
            }
        }
        stage('Testing Stage') { 
            steps {
                withMaven(maven : 'maven_3_6_3') {
                 sh 'mvn test'
            }
        }
     }
        stage ('Deployment Stage') { 
            steps {
                withMaven(maven : 'maven_3_6_3') {
                 sh 'mvn deploy'
            }
        }
    }


*/

/*
pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            echo 'Hello World'
            echo 'All Good in da Hood'
         }
      }
   }
}
*/

pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Starting Backup!"
                sh "sh /test/backup.sh"
            }
        }
    }
}