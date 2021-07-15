pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
        DATABASE_URI = credentials('DATABASE_URI')
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
                }
            }
        }
        stage('Build Images'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        sh 'docker-compose build'
                        image = docker.image("bludobson/song_server:${env.app_version}")
                        }
                        
                    }
                }
            }
        stage('Push images'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            image.push()
                        }
                    }
                }
            }
        }
        stage('Deploy app'){
            steps{
                dir('ansible'){
                    sh 'ansible-playbook -i inventory.yaml playbook.yaml'
                }
            }
        }
    }
}