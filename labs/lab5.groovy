
node {
    try {
        def runStage = { stageName, command ->
    stage(stageName) {
        echo "Starting stage: ${stageName}"
        sh command
    }
    }
>>>>>>> 49dae5a6ea8ccffd3befe66f27e8a99397573d3b
        // Stage for cloning the repository
        stage('Clone') {
            runStage('Clone', 'echo "cloning repository..."')
        }

        // Stage for building the project
        stage('Build') {
            runStage('Build', 'echo "building python project..."')
        }

        // Running linting and security checks in parallel
        parallel(
            'Lint': {
                runStage('Lint', 'echo "Running Python linting..."')
            },
            'Security test': {
                runStage('Security test', 'echo "Running security checks (e.g, safety)"')
            }
        )

        // Stage for deployment with user input
        stage('Deploy') {
            script {
                def userInput = input message: 'Do you want to proceed with deployment?', 
                                      parameters: [choice(name: 'Approve', choices: ['Proceed', 'Abort'], description: 'Select Proceed to deploy, Abort to cancel.')]

                if (userInput == 'Proceed') {
                    runStage('Deploy', 'echo "Deploying Python project to production..."')
                } else {
                    error 'Deployment aborted by user!'
                }
            }
        }

        // Cleanup stage
        stage('Cleanup') {
            runStage('Cleanup', 'echo "Cleaning up workspace..."')
        }

        echo "All stages completed"
        
    } catch (Exception e) {
        echo "Error in one of the stages: ${e.message}"
    }
<<<<<<< HEAD
}
=======
}
>>>>>>> 49dae5a6ea8ccffd3befe66f27e8a99397573d3b
