# Expert System API

## Introduction
This project is an expert system API for diagnosing car problems. The API is built using Django REST Framework and the logic is implemented using the `aima3` library for artificial intelligence. The system diagnoses car problems based on a set of symptoms or signs provided by the user.

## Setup Steps

1. **Clone the project**: Clone the project from GitHub using the following command:

```bash
git clone https://github.com/Chouaib-Djerdi/Expert-System-API.git
```

2. **Activate the virtual environment**: If you're using conda, you can create a new environment and activate it using the following commands:

```bash
conda create --name myenv
conda activate myenv
```

3. **Install dependencies**: Navigate to the project directory and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

4. **Navigate to the backend directory**: Use the following command:

```bash
cd Expert-System-API/backend
```

5. **Run the server**: You can start the Django server using the following command:

```bash
python manage.py runserver
```

## Explanation of the `diagnose_problem` Function

The `diagnose_problem` function in `utils.py` is the core of the expert system. It takes a list of signs as input and returns the most likely problem based on the signs. Here's a brief explanation of how it works:

- It initializes an agenda and a memory. The agenda stores the signs to be processed, and the memory stores the confirmed signs.

- It adds the input signs to the agenda.

- It runs a loop to process each sign in the agenda. For each sign, it checks if the sign is confirmed (i.e., it matches a sign in the knowledge base). If the sign is confirmed, it's added to the memory.

- After all signs are processed, it calculates a score for each problem based on the number of matching signs. The score is the ratio of the number of matching signs to the total number of signs associated with the problem.

- Finally, it returns the problem with the highest score.

## Populating the Database

You can populate the database with problems and signs using the Django admin interface. Here's how:

1. **Create a superuser**: If you haven't already, create a superuser for your Django project using the following command:

```bash
python manage.py createsuperuser
```

2. **Log in to the admin interface**: Start your Django server and navigate to `http://localhost:8000/admin` in your web browser. Log in with your superuser credentials.

3. **Add problems and signs**: In the admin interface, you can add `Problem` and `Sign` instances. Each `Problem` instance should have a name, a description, solutions, and associated signs. Each `Sign` instance should have a name.

Remember to test your API thoroughly to ensure it works as expected. Good luck with your project! 😊
