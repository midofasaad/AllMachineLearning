# How to make me work? (Virtual Enviroment & Package Management):

1.  Run the batch file "opencmd.bat" to install the virtual enviroment "venv", which will automatically install all required dependencies from requirements.txt.
2.  For a fast installation of  new dependencies, use this batch file. It will open a cmd window and automatically activate the virtual enviroment.    
2.  Any new dependencies can be added into the dependencies file "requirements.txt".
# How to use me? (Project Structure): 
* LinearRegression.py : Perfrom and visualize Polynomial Regression given a sample of observations as a numpy vector [yObs] and their corresponding input numpy vector [xSample]. xSample is extended into a design Matrix XSample, which is then used with the reqiured polynomial degree [pDeg] to return a weights vector [w]. Given yFit=wx, yFit is calculated. 
* BayesianRegression.py: Perform Bayesian Regression given a sample of observations, their corresponding input, estimated variance [sigma] and preciscion of the weights [alpha] (Assumption: Gaussian Prior of the weights).
* ScientificMachineLearning.py: Sample for the graphical representation of dependencies between random variables. 