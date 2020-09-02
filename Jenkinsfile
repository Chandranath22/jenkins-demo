def bucket = 'jenkins-demo-101'
def region = 'ap-south-1'
def functionName = 'calculator.py'

pipeline {
  agent any
    stages {
      stage('Test'){
        echo '******************* Testing ************************'
        python calculator/test_calc.py
      }
    }
}
