# SecureCheck

Web app that uses machine learning to classify that strength of a password.

## Description

Built using Svelte, Python, Scikit-Learn, and Flask, this web app will use real data and machine learning to classify the strength of a password. The data set comes from [here](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset) and is classified using a tool developed by Georgia Tech called PARS. The passwords for the dataset come from publicly sourced databreaches. The password strength falls into one of three catergories, weak, medium, and strong. The model used to predict the dataset is a simple logistic regression that tokenizes the input. Accuracy for the model sits at around 82%. Further development would include adding to the dataset, training and testing with neural networks, and deploying to the web.

## Getting Started

### Dependencies

* ```python, npm, flask, scikit-learn```

### Installing

* To install for the frontend, go to the ```/Frontend``` directory and do ```npm install```.
* To install for the backend, got to the ```/Backend``` directory and either use ```pip``` to install ```scikit-learn & flask``` or use a virtual environment, ```python -m .venv <name>```.

### Executing program

* To start the frontend, go to the ```/Frontend``` directory and do ```npm run dev```.
* To start the backend, go to the ```/Backend``` directory and do ```flask --app server.py run```.

## Help

* Please contact me at my socials for any assitance.

## Authors

* Cameron McConnell
* [LinkedIn](https://www.linkedin.com/in/cameron-mcconnell-704b17225/)
* cameron.mcconne@gmail.com

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [Dataset](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset)
