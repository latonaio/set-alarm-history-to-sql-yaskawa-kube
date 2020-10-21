FROM latonaio/l4t:latest

# Definition of a Device & Service
ENV POSITION=Runtime \
    SERVICE=set-alarm-history-to-sql-yaksawa \
    AION_HOME=/var/lib/aion \
    LC_CTYPE=ja_JP.UTF-8

RUN mkdir -p {AION_HOME}
WORKDIR ${AION_HOME}

RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8 && export LC_CTYPE="ja_JP.UTF-8"

# Setup Directoties
RUN mkdir -p $POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/
ADD . .
RUN python3 setup.py install
CMD ["python3", "-m", "set-alarm-history-to-sql"]
