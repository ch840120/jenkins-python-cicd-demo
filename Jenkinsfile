pipeline {
    agent any

    environment {
        IMAGE_NAME = "localhost:5000/jenkins-python-cicd-demo:${BUILD_NUMBER}"  // Tag 為 Build 號碼
    }

    stages {
        stage('Clone') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-ssh-key', url: 'git@github.com:ch840120/jenkins-python-cicd-demo.git']])
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    sh "docker push ${IMAGE_NAME}"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh """
                    # 移除舊容器（如果存在）
                    docker stop jenkins-python-cicd-demo || true
                    docker rm jenkins-python-cicd-demo || true
                    # 拉最新 image
                    docker pull ${IMAGE_NAME}
                    # 啟動新容器，9001:9001
                    docker run -d --name jenkins-python-cicd-demo -p 9001:9001 ${IMAGE_NAME}
                    """
                }
            }
        }

        stage('Clean Images') {
            steps {
                script {
                sh '''
                # 清掉 dangling/untagged images
                docker image prune -f

                # 列出 repo:tag，只挑我們的 repo，排除當前 BUILD_NUMBER
                docker images --format '{{.Repository}}:{{.Tag}}' | \
                    grep '^localhost:5000/jenkins-python-cicd-demo:' | \
                    grep -v ":${BUILD_NUMBER}$" | \
                    xargs -r docker rmi -f || true
                '''
                }
            }
        }
    }
}