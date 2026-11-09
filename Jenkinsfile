pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Preparando proyecto Flask...'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat 'py -m pytest -v'
            }
        }

        stage('Generate Documentation') {
            steps {
                echo 'Generando documentación con Doxygen...'
                bat 'doxygen Doxyfile'
            }
        }

        stage('Version Control') {
            steps {
                echo 'Preparando documentacion para Git...'
                bat 'git add -f docs/html'
                bat 'git status'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Construyendo imagen Docker...'
                bat 'docker build -t actividad-documentacion-flask .'

                echo 'Desplegando aplicacion...'
                bat 'docker rm -f actividad-documentacion-flask || exit /b 0'
                bat 'docker run -d --name actividad-documentacion-flask -p 5001:5000 actividad-documentacion-flask'
            }
        }
    }
}