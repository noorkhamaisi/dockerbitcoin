FROM python

COPY requirments.txt .
RUN pip install -r requirments.txt 

COPY main.py .

CMD ["python","main.py"]
