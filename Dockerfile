FROM python:3.10.14
SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade "pip==24.0"

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash user && chmod 777 /opt /run

WORKDIR /FinanceApp

RUN chown -R user:user /FinanceApp && chmod 755 /FinanceApp

COPY --chown=user:user . .

RUN pip install -r requirements.txt

USER user

CMD ["gunicorn", "-b", "0.0.0.0:8001", "finance_project/wsgi.application"]