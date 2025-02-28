node {


  def runStage = { stageName, command ->
        stage(stageName) {
            echo "Starting stage: ${stageName}"
            sh command
        }
    }


    stage('Clone'){
        runStage('Clone',  'echo "cloning repostry..."')
       
    }

    stage('Build'){
        runStage('Buiild', 'echo "building python project..."')
       
    }


    parallel{
        
        stage('Lint'){
            runStage('Lint', 'echo "Running Pyhthon linting"')
            
        }

        stage('Security test'){
            runStage('Security test', 'echo "Running security checks (e.g, safety)"')
        }

    }

  

    stage('Deploy'){

          steps {
            script {
                def userInput = input message: 'Do you want to proceed with deployment?', 
                                     parameters: [choice(name: 'Approve', choices: 'Proceed\nAbort', description: 'Select Proceed to deploy, Abort to cancel.')]

                if (userInput == 'Proceed') {
                    runStage('Deploy', 'echo "Deploying Python project to production..."')
                    

                } else {
                    error 'Deployment aborted by user!'
                }
            }
        }
    }



    stage('Cleanup') {
    runStage('Cleanup', 'echo "Cleaning up workspace..."')
    }
}



