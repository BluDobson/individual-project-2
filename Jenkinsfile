pipeline{
    agent any
    environment {
        DATABASE_URI = credentials('DATABASE_URI')
        docker_password = credentials('docker_password')
        str_len = '4'
    }
    stages{
        stage('Test Build'){
            steps{
                script{
                    sh 'python3 -m venv venv'
                    sh '. ./venv/bin/activate'
                    sh 'pip3 install -r requirements.txt'
                    sh 'pip3 freeze'
                    sh 'python3 -m pytest ./server --cov=app --cov-report html:s1_html'
                    sh 'python3 -m pytest ./artist_api --cov=app --cov-report html:s2_html'
                    sh 'python3 -m pytest ./random_api --cov=app --cov-report html:s3_html'
                    sh 'python3 -m pytest ./song_api --cov=app --cov-report html:s4_html'
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 's1_html', reportFiles: 'index.html', reportName: 'Server Coverage', reportTitles: ''])
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 's2_html', reportFiles: 'index.html', reportName: 'Artist_Api Coverage', reportTitles: ''])
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 's3_html', reportFiles: 'index.html', reportName: 'Random_Api Coverage', reportTitles: ''])
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 's4_html', reportFiles: 'index.html', reportName: 'Song_Api Coverage', reportTitles: ''])
                }
            }
        }
        stage('Build Images'){
            steps{
                script{
                    sh 'docker-compose build'
                    }
                }
            }
        stage('Push images'){
            steps{
                script{
                    sh 'docker login -u bludobson -p ${docker_password}'
                    sh 'docker system info | grep -E "Username|Registry"'
                    sh 'docker push bludobson/song_server:latest'
                    sh 'docker push bludobson/artist_api:latest'
                    sh 'docker push bludobson/random_api:latest'
                    sh 'docker push bludobson/song_api:latest'
                }
            }
        }
        stage('Deploy app'){
            steps{
                sh './docker-compose.sh'
                sh 'scp docker-compose1.yaml jenkins@swarm-manager:~/'
                sh 'ssh -o StrictHostKeyChecking=no jenkins@swarm-manager "docker stack deploy --compose-file docker-compose1.yaml song-stack"'
            }
        }
    }
}