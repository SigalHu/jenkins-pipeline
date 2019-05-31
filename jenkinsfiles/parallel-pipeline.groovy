/**
 * @author huxujun
 * @date 2019-05-31
 */

pipeline {
    agent any

    // 注入环境变量
    environment {
        ACCESS_KEY = credentials('40b821ba-acf1-40cc-93ee-d34edd16199e')
        PYTHONPATH = "${WORKSPACE}/scripts"
    }

    stages {
        stage('checkout scripts') {
            input {
                message "Input git repo branch!"
                ok "OK"
                parameters {
                    string(name: 'branch', defaultValue: 'master', description: 'branch')
                }
            }
            steps {
                sh "rm -rf ${WORKSPACE}/*"
                dir('scripts') {
                    git branch: "${branch}", url: 'git@github.com:SigalHu/jenkins-pipeline.git'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('print envs') {
            input {
                message "Input some message!"
                ok "OK"
                parameters {
                    string(name: 'message1', defaultValue: 'value1', description: 'Input message1!')
                    string(name: 'message2', defaultValue: 'value2', description: 'Input message2!')
                }
            }
            steps {
                dir('scripts') {
                    echo 'print envs...'
                    sh "python3 scripts/print_envs.py"
                }
            }
        }
        stage('print dirs') {
            steps {
                dir('scripts') {
                    echo 'print dirs...'
                    sh "python3 scripts/print_dirs.py"
                }
            }
        }
        stage('ssh connect') {
            steps {
                dir('scripts') {
                    echo 'test ssh connect...'
                    sh "python3 scripts/ssh_connect.py"
                }
            }
        }
        stage('delete file') {
            input {
                message "Make some choices!"
                ok "OK"
                submitter "sigalhu"
                parameters {
                    choice(name: 'delete_file', choices: 'YES\nNO\n', description: 'Delete jenkins_pipeline_LICENSE?')
                }
            }
            when {
                environment name: 'delete_file', value: 'YES'
            }
            steps {
                script {
                    def remote = [name: 'localhost', 'host': '127.0.0.1', 'user': "${ACCESS_KEY_USR}", 'port': 22, 'identityFile': "${ACCESS_KEY}", 'allowAnyHosts': true]
                    echo 'delete file...'
                    sshRemove remote: remote, path: "jenkins_pipeline_LICENSE"
                    sh "ssh ${ACCESS_KEY_USR}@127.0.0.1 -o stricthostkeychecking=no \"ls\""
                }
            }
        }
    }
}
