pipeline {
    agent any // Exécute le pipeline sur n'importe quel agent Jenkins disponible

    stages {
        stage('Récupération du code') {
            steps {
                echo 'Clonage du dépôt GitHub...'
                // Remplacez l'URL par celle de votre propre dépôt GitHub
                git branch: 'main', url: 'https://github.com/amadypabamemaths-cpu/projet-bibliotheque-dit.git'
            }
        }

        stage('Construction (Build)') {
            steps {
                echo 'Construction des images Docker pour le Backend et le Frontend...'
                // Exécute la construction des images définies dans docker-compose.yml
                sh 'docker compose build'
            }
        }

        stage('Déploiement (Deploy)') {
            steps {
                echo 'Lancement des conteneurs avec Docker Compose...'
                // Lance les conteneurs en arrière-plan (-d)
                sh 'docker compose up -d'
            }
        }
    }

    post {
        success {
            echo 'Le pipeline a été exécuté avec succès ! L\'application est déployée.'
        }
        failure {
            echo 'Le pipeline a échoué. Veuillez vérifier les logs.'
        }
    }
}