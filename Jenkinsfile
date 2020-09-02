def bucket = 'jenkins-demo-101'
def region = 'ap-south-1'
def functionName = 'calculator.py'

pipeline {
  agent any
    stages {
      stage('Test'){
        steps {
          echo '******************* Testing ************************'
          bat label: 'testing', script: 'python calculator/test_calc.py'
        }
      }
    }
}
