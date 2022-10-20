FROM python:3
RUN git clone https://github.com/perezmatias/CRUD-Persona.git
WORKDIR /CRUD-Persona
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]