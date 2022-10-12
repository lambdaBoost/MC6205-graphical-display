FROM python:3.9

WORKDIR /code

COPY imgs/ /code/imgs

COPY api_tools /code/api_tools

COPY ./requirements.txt /code/requirements.txt 

COPY ./main.py /code/

RUN apt-get update

# RUN apt-get install -y libatlas-base-dev

# RUN pip3 install --upgrade pip setuptools wheel

RUN pip install --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
