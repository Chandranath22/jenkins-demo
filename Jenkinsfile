def bucket = 'jenkins-demo-101'
def region = 'ap-south-1'
def functionName = 'calculator.py'

pipeline {
  agent any
    stages {
      stage ('Test'){
        steps {
          echo '******************* Testing ************************'
          bat label: 'testing', script: 'python calculator/test_calc.py'
        }
      }

      stage ('Build SAM package'){
        steps {
          echo '******************* Building *************************'
          bat label: 'Sam building', script: 'sam build'
        }
      }

      stage ('Deploying SAM template'){
        steps {
          echo '******************* Building *************************'
          bat label: 'Sam deploying', script: 'sam deploy --stack-name calc-demo --region ap-south-1 --capabilities CAPABILITY_IAM --confirm-changeset true'
        }
      }
    }
}
