FROM python:3.10-slim AS base
WORKDIR /secondweek

FROM base AS tinistage
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]
COPY ./requirements.txt /secondweek/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /secondweek/requirements.txt

FROM tinistage AS stage3
COPY ./app /secondweek/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]