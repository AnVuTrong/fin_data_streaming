FROM python:3.12

WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3
ENV PATH="/opt/poetry/bin:$PATH"
RUN poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml ./poetry.lock* /

# Allow installing dev dependencies to run tests
RUN bash -c "poetry install --no-root"

COPY . .

EXPOSE 7777

CMD ["python", "src/main.py"]
