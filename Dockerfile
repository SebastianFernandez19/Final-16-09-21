FROM python:3
RUN git clone https://github.com/SebastianFernandez19/Final-16-09-21.git
RUN pip install pip
RUN pip install parameterized
WORKDIR /Final-16-09-21
CMD ["python3","-m","unittest"]
