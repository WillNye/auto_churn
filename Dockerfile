FROM python:3.6

ENV repoDir /var/app/churning

RUN apt-get -y update && apt-get install -y \
    git

# So, I know what you're thinking "this guy is copying everything down there why not do that and install?"
# Because now I don't have to wait for installs making build time super fast
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p ${repoDir}
WORKDIR ${repoDir}
ARG CACHEBREAK=1

COPY . .

RUN ["chmod", "+x", "entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
