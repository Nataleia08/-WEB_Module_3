FROM python:3.10

WORKDIR $WEB_Module_2

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "menu.py"]

VOLUME ./data:/data