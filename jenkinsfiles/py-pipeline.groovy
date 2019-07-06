/**
 * @author huxujun
 * @date 2019-05-31
 */
pipeline {
    agent any

    // 注入环境变量
    environment {
        ACCESS_KEY = credentials('40b821ba-acf1-40cc-93ee-d34edd16199e')
//        PYTHONPATH = "${WORKSPACE}/scripts"
        PYTHONPATH = "${WORKSPACE}"
//        OUTPUT = "${WORKSPACE}/output/${JOB_NAME}"
    }

    parameters {
        choice(name: 'random_choice', choices: randomChoice(), description: 'This is a random choice!')
        choice(name: 'random_choice2', choices: ['1', '2', '3'], description: 'This is a random choice2!')
        string(name: 'message3', defaultValue: 'test123', description: 'Input message3!')
        string(name: 'message4', defaultValue: 'value4', description: 'Input message4!')
    }

    stages {
        stage('checkout scripts') {
//            input {
//                message "Input git repo branch!"
//                ok "OK"
//                parameters {
//                    string(name: 'branch', defaultValue: 'master', description: 'branch')
//                }
//            }
            steps {
//                sh "rm -rf ${WORKSPACE}/*"
//                dir('scripts') {
//                    git branch: "${branch}", url: 'git@github.com:SigalHu/jenkins-pipeline.git'
                    sh 'pip3 install -r requirements.txt'
//                }
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
//                dir("${OUTPUT}"){
//                    writeFile encoding: 'utf-8', file: 'params.message1', text: "${params.message1}"
//                    writeFile encoding: 'utf-8', file: 'params.message2', text: "${params.message2}"
//                }
//                dir('scripts') {
                    echo 'print envs...'
                    sh "python3 scripts/print_envs.py"
//                }
            }
        }
        stage('print dirs') {
            steps {
//                dir('scripts') {
                    echo 'print dirs...'
                    sh "python3 scripts/print_dirs.py"
//                }
            }
        }
        stage('ssh connect') {
            steps {
//                dir('scripts') {
                    echo 'test ssh connect...'
                    sh "python3 scripts/ssh_connect.py"
//                }
            }
        }
        stage('delete file') {
            input {
                message "Make some choices!"
                ok "OK"
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
        stage('exec python') {
            steps {
                script {
                    echo 'start to exec print_envs.py by groovy script...'
                    println 'pwd'.execute().text
                    def proc = "python3 ${PYTHONPATH}/scripts/print_envs.py".execute(["PYTHONPATH=${PYTHONPATH}"], null)
                    proc.waitFor()
                    println "stdout: ${proc.in.text}"
                    println "stderr: ${proc.err.text}"
                    echo 'end to exec print_envs.py by groovy script'
                }
            }
        }
    }
    post {
        always {
            echo 'test save user config...'
            sh "python3 scripts/save_user_config.py xujun sigal"
        }
    }
}

static String randomChoice() {
    Random random = new Random()
    StringBuilder sb = new StringBuilder()
    sb.append(random.nextInt())
    sb.append('\n')
    sb.append(random.nextInt())
    sb.append('\n')
    sb.append(random.nextInt())
    sb.append('\n')
    return sb.toString()
}
