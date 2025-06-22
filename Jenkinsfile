pipeline{
    agent any 

    environment{
        VENV_DIR ='venv'
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins.......................'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/hariom845/End-to-End-Hotel-Reservation-Prediction-with-MLFlow-Jenkins-and-GCP-Deployment.git']])
                }
            }
        }

        stage('Setting up our Virtul Environment and Installing dependancies'){
            steps{
                script{
                    echo 'Setting up our Virtul Environment and Installing dependancies......................'
                    sh '''
                    python -m venv ${VENV_DIR}
                    .$(VENV_DIR)/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}
