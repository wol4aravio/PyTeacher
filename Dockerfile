FROM python:3.8.6-slim as prod

RUN pip3 install poetry

WORKDIR /source
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev

COPY pyteacher pyteacher
RUN poetry install --no-dev

ENTRYPOINT [ "poetry", "run" ]



FROM prod as test

RUN poetry install

WORKDIR /source
COPY tests tests
COPY .coveragerc .coveragerc

ENTRYPOINT [ "poetry", "run" ]
