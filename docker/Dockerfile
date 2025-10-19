FROM python:3.11-slim as base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

FROM base as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

FROM base as final
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . /app
ENV PATH="/usr/local/bin:$PATH"
RUN useradd -m appuser && chown -R appuser /app
USER appuser
ENV DJANGO_SETTINGS_MODULE=qro_project.settings
RUN mkdir -p /app/staticfiles
CMD ["gunicorn", "qro_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
