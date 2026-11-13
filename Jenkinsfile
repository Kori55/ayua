pipeline {
    agent any

    stages {
	stage('Verificar Python') {
		steps {
			bat 'where python'
			bat 'python --version'
		}
	}

        stage('Build') {
            steps {
                echo 'Preparando proyecto Flask...'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat 'python -m pytest -v'
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

                bat 'git rm -r --cached --ignore-unmatch __pycache__'
                bat 'git add -f docs/html'
                bat 'git add .gitignore'

                script {
                    def cambios = bat(
                        script: 'git diff --cached --quiet',
                        returnStatus: true
                    )

                    if (cambios != 0) {
                        bat 'git config user.name "Jenkins"'
                        bat 'git config user.email "jenkins@localhost"'
                        bat 'git commit -m "Actualizar documentacion generada"'

                        withCredentials([gitUsernamePassword(
                            credentialsId: 'github-ayua',
                            gitToolName: 'Default'
                        )]) {
                            bat 'git push origin HEAD:main'
                        }
                    } else {
                        echo 'No hay cambios nuevos en la documentacion.'
                    }
                }
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