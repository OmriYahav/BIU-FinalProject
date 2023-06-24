pipeline{
    agent {
        docker{
            image 'elirazo/pingpong-app'
            args '-p 5005:5005 -u root'
        }
    }
    parameters{
        string(name:'NAME',defaultValue:'',description:'pingPongApp')
    }
    stages{
        stage('checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/OmriYahav/-BIU-FinalProject']]])
            }
        }
        stage('build'){
            steps{
                sh 'docker image build -t pingpong:v3'
                sh 'python3 app.py &'
            }
           
        }
        stage('test'){
            steps{
                sh 'pytest test.py'
            }
           
        }
        stage('build an image'){
            when{
                branch 'dev'
            }

            steps{
                sh 'echo build image'
            }
           
        }  
        stage('post'){
            steps{
                echo "post $params.NAME"
            }
           
        }
    }
}
