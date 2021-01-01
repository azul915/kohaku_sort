FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
    git unzip python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/share/fonts
ENV RICTY_DIMINISHED_VERSION 3.2.4
ADD https://github.com/mzyy94/RictyDiminished-for-Powerline/archive/$RICTY_DIMINISHED_VERSION-powerline-early-2016.zip .
RUN unzip -jo $RICTY_DIMINISHED_VERSION-powerline-early-2016.zip && \
    fc-cache -fv

COPY ./app/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /etc
RUN echo "backend : Agg" >> matplotlibrc && \
    echo "font.family : Ricty Diminished" >> matplotlibrc

WORKDIR /opt/app
ENV MATPLOTLIB_VERSION 2.0.2
RUN pip install matplotlib==$MATPLOTLIB_VERSION

CMD ["python", "main.py"]