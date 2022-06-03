pipeline {
    agent any

    stages {
        steps {
            sh'''
            python3 main.py $day $month $year
            '''
        }

        steps {
            sh'''
            echo 
            '''
        }
    }
}