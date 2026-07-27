// Jenkinsfile - equivalente do pipeline de CI no Jenkins (Declarative Pipeline)
// Desafio Nível 3: mesmo lint + testes que o GitHub Actions faz, agora no Jenkins.
pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependências') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint (flake8)') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 src/ tests/ --max-line-length=100
                '''
            }
        }

        stage('Testes (pytest + cobertura)') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v --cov=src --cov-report=term-missing
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline verde: lint e testes passaram.'
        }
        failure {
            echo 'Pipeline vermelha: verifique o log do estágio que falhou.'
        }
    }
}
