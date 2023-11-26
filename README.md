## Getting Started


### Requirements
- Python 3
- NPM

Install the python dependencies:

```bash
pip install -r requirements.txt
```

Install the js dependencies:

```bash
npm install
```

Then, run the development server:

#### 1. Start the flask project

```bash
python3 run.py
```

#### 2. Start tailwind builder

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```