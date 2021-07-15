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
                    sh 'pip install -r requirements.txt'
                    pysh 'pytest ./server --cov=app --cov-report html:s1_html'
                    pysh 'pytest ./artist_api --cov=app --cov-report html:s2_html'
                    pysh 'pytest ./random_api --cov=app --cov-report html:s3_html'
                    pysh 'pytest ./song_api --cov=app --cov-report html:s4_html'
                }
            }
        }
        stage('Build Images'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        s1 = docker.build("bludobson/song_server")
                        s2 = docker.build("bludobson/artist_api")
                        s3 = docker.build("bludobson/random_api")
                        s4 = docker.build("bludobson/song_api")
                    }
                }
            }
        }
        stage('Tag and push images'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            s1.push("${env.app_version}")
                            s2.push("${env.app_version}")
                            s3.push("${env.app_version}")
                            s4.push("${env.app_version}")
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