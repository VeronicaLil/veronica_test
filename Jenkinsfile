pipeline {
    agent any

    stages {
        stage ("ESEGUI FILE") {
            steps {
                sh'''
                python3 main.py $day $month $year ${years_to_add}
                '''
            }
        }

        stage ("EXTRA") {

            steps {
                sh'''
                echo $year   
                '''
            }
        }
    }
}
