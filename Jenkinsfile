pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }
    stages{
        stage('Test Build'){
            steps{
                sh 'pytest ./server --cov=app --cov-report html:s1'
                sh 'pytest ./artist_api --cov=app --cov-report html:s2'
                sh 'pytest ./random_api --cov=app --cov-report html:s3'
                sh 'pytest ./song_api --cov=app --cov-report html:s4'
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