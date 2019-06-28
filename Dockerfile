FROM python:3.6

# Work directory
ADD . /scrap_heyjobs
WORKDIR /scrap_heyjobs

# To install requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5432

CMD [ "python", "run.py" ]